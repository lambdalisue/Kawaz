from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()
#import drafts
#drafts.autodiscover()
#import calls
#calls.autodiscover()

from views import IndexView

urlpatterns = patterns('',
    #url(r'^$',              IndexView.as_view(), name='index'),
    url(r'^$',              'socialauth.views.signin_complete'),
    url(r'^accounts/',      include('socialauth.urls')),
    url(r'^admin/doc/',     include('django.contrib.admindocs.urls')),
    url(r'^admin/',         include(admin.site.urls)),
    url(r'^announcements/', include('Kawaz.announcements.urls')),
)