# -*- coding:utf-8 -*-
from django import template
from django.template import TemplateSyntaxError

from ..models import Announcement

register = template.Library()

class GetAnnouncementsAs(template.Node):
    def __init__(self, variable_name):
        self.variable_name = variable_name

    def render(self, context):
        request = template.resolve_variable('request', context)
        # Sageが設定されていない公開されたお知らせをすべて取得する
        context[self.variable_name] = Announcement.objects.published(request).exclude(sage=True)
        return ''

@register.tag
def get_announcements(parser, token):
    u"""お知らせの一覧を表示
    
    Usage:
        {% get_announcements to <variable> %}
    
    """
    bits = token.split_contents()
    if len(bits) == 3:
        if bits[1] != 'to':
            raise TemplateSyntaxError("first argument to %r tag must be 'to'" % bits[0])
        variable_name = bits[2]
        return GetAnnouncementsAs(variable_name)
    raise TemplateSyntaxError("%r tag must has two arguments (%d given)" % (bits[0], len(bits)))
