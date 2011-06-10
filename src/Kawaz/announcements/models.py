# -*- coding: utf-8 -*-
from django.contrib.auth.models import User

from django.db import models
from markupfield.fields import MarkupField
from qwert.middleware import threadlocals

import datetime

class AnnouncementManager(models.Manager):
    def published(self, request):
        if request and request.user.is_authenticated():
            return self.exclude(pub_state='draft')
        else:
            return self.filter(pub_state='public')
    def draft(self, request):
        if request and request.user.is_authenticated():
            return self.filter(pub_state='draft', author=request.user)
        else:
            return self.none()
        
class Announcement(models.Model):
    u"""運営からのお知らせ用モデル"""
    PUB_STATES = (
        ('public',      u"外部公開"),
        ('protected',   u"内部公開"),
        ('draft',       u"下書き"),
    )
    # Required
    pub_state       = models.CharField(u"公開範囲", max_length=10, choices=PUB_STATES, default='public')
    title           = models.CharField(u"タイトル", max_length=128)
    body            = MarkupField(u"本文", default_markup_type='markdown')
    sage            = models.BooleanField(u"Sage", default=False, 
                                          help_text=u"チェックを入れるとトップページのお知らせに表示させません。"
                                                    u"また各ユーザーに対する通知も飛ばしません")
    # Uneditable
    author          = models.ForeignKey(User, related_name='created_announcements')
    updated_by      = models.ForeignKey(User, related_name='updated_announcements')
    created_at      = models.DateTimeField(u"作成日時", auto_now_add=True)
    updated_at      = models.DateTimeField(u"更新日時", auto_now=True)
    publish_at      = models.DateTimeField(u"公開日時", null=True, editable=False)
    publish_at_date = models.DateField(u"公開日", null=True, editable=False)
    objects         = AnnouncementManager()
    
    class Meta:
        ordering            = ('-created_at',)
        verbose_name        = u"お知らせ"
        verbose_name_plural = verbose_name
    
    def __unicode__(self):
        return self.title
    
    @models.permalink
    def get_absolute_url(self):
        if self.pub_state == 'draft':
            # 公開状態が下書きの場合は直で編集ページを返す
            return ("announcements-announcement-update", (), {'object_id': self.pk})
        return ("announcements-announcement-detail", (), {'object_id':self.pk})
    
    def clean(self, *args, **kwargs):
        created = self.pk is None
        request = threadlocals.request()
        if created and request:
            # 著者の自動設定 (テストなど request が存在しない場合はシステムユーザーを適用)
            self.author = request.user if request else User.objects.get(pk=1)
        # 下書き関係のValidation
        if self.pub_state == 'draft' and self.publish_at:
            self.publish_at = None
            self.publish_at_date = None
        elif self.pub_state != 'draft' and not self.publish_at:
            self.publish_at = datetime.datetime.now()
            self.publish_at_date = datetime.date.today()
        # 更新者の自動設定
        self.updated_by = request.user if request else User.objects.get(pk=1)
    
    def modify_object_permission(self, mediator, created):
        mediator.manager(self, self.author)
        if self.pub_state == 'draft':
            mediator.reject(self, None)
            mediator.reject(self, 'anonymous')
        elif self.pub_state == 'protected':
            mediator.viewer(self, None)
            mediator.reject(self, 'anonymous')
        else:
            mediator.viewer(self, None)
            mediator.viewer(self, 'anonymous')