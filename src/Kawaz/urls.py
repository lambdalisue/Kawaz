from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from views import IndexView

urlpatterns = patterns('',
    url(r'^$',              IndexView.as_view(), name='index'),
    url(r'^admin/doc/',     include('django.contrib.admindocs.urls')),
    url(r'^admin/',         include(admin.site.urls)),
    url(r'^announcements/', include('Kawaz.announcements.urls')),
)