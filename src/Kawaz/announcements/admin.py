# -*- coding: utf-8 -*-
#
# from snippets: http://djangosnippets.org/snippets/1054/
#
from django.contrib import admin
from models import Announcement

class AnnouncementAdmin(admin.ModelAdmin):
    date_hierarchy  = 'created_at'
    list_display = ('title', 'author', 'sage', 'publish_at', 'created_at', 'updated_at')
    list_filter = ('author', 'created_at', 'updated_at', 'publish_at')
    search_fields = ('title', 'body', 'author',)
    
    def queryset(self, request):
        qs = super(AnnouncementAdmin, self).queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            return qs.filter(author = request.user)
    
admin.site.register(Announcement, AnnouncementAdmin)
