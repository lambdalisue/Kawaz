# -*- coding: utf-8 -*-
#
# Created:    2010/09/24
# Author:         alisue
#
from django.conf.urls.defaults import patterns, url

import views

urlpatterns = patterns('',
    url(r'^$',            views.draft_list,    name='drafts-draft-list'),
)
