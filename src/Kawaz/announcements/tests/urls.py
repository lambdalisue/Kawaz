# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url

from ..views import AnnouncementListView
from ..views import AnnouncementDetailView
from ..views import AnnouncementYearArchiveView
from ..views import AnnouncementMonthArchiveView
from ..views import AnnouncementCreateView
from ..views import AnnouncementUpdateView
from ..views import AnnouncementDeleteView

urlpatterns = patterns('',
    url(r'^$', AnnouncementListView.as_view(), name='announcements-announcement-list'),
    url(r'^(?P<pk>\d+)/$', AnnouncementDetailView.as_view(), name='announcements-announcement-detail'),
    url(r'^archive/(?P<year>\d{4})/$', AnnouncementYearArchiveView.as_view(), name='announcements-announcement-archive-year'),
    url(r'^archive/(?P<year>\d{4})/(?P<month>\d{1,2})/$', AnnouncementMonthArchiveView.as_view(), name='announcements-announcement-archive-month'),
    url(r'^create/$', AnnouncementCreateView.as_view(), name='announcements-announcement-create'),
    url(r'^(?P<pk>\d+)/update/$', AnnouncementUpdateView.as_view(), name='announcements-announcement-update'),
    url(r'^(?P<pk>\d+)/delete/$', AnnouncementDeleteView.as_view(), name='announcements-announcement-delete'),
)