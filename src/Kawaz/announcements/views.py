# -*- coding: utf-8 -*-
#
# Author:        alisue
# Date:            2010/11/30
#
from django.core.urlresolvers import reverse
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import YearArchiveView
from django.views.generic import MonthArchiveView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from object_permission.decorators import permission_required

from forms import AnnouncementForm
from models import Announcement

class AnnouncementListView(ListView):
    def get_queryset(self):
        qs = Announcement.objects.published(self.request)
        return qs
    
class AnnouncementDetailView(DetailView):
    def get_queryset(self):
        qs = Announcement.objects.published(self.request)
        return qs
    @method_decorator(permission_required('announcements.view_announcement', Announcement))
    def dispatch(self, request, *args, **kwargs):
        return super(AnnouncementDetailView, self).dispatch(request, *args, **kwargs)

class AnnouncementYearArchiveView(YearArchiveView):
    date_field = 'updated_at'
    allow_empty = True
    def get_queryset(self):
        qs = Announcement.objects.published(self.request)
        return qs
class AnnouncementMonthArchiveView(MonthArchiveView):
    date_field = 'updated_at'
    month_format = '%m'
    allow_empty = True
    def get_queryset(self):
        qs = Announcement.objects.published(self.request)
        return qs

class AnnouncementCreateView(CreateView):
    form_class = AnnouncementForm
    model = Announcement
    
    @method_decorator(permission_required('announcements.add_announcement'))
    def dispatch(self, request, *args, **kwargs):
        return super(AnnouncementCreateView, self).dispatch(request, *args, **kwargs)
    
class AnnouncementUpdateView(UpdateView):
    form_class = AnnouncementForm
    
    def get_queryset(self):
        qs = Announcement.objects.all()
        return qs
    
    # To enable update via staff, not using object permission
    @method_decorator(permission_required('announcements.change_announcement'))
    def dispatch(self, request, *args, **kwargs):
        return super(AnnouncementUpdateView, self).dispatch(request, *args, **kwargs)
class AnnouncementDeleteView(DeleteView):
    model = Announcement
    
    def get_success_url(self):
        return reverse('announcements-announcement-list')
    
    # To enable delete via staff, not using object permission
    @method_decorator(permission_required('announcements.delete_announcement'))
    def dispatch(self, request, *args, **kwargs):
        return super(AnnouncementDeleteView, self).dispatch(request, *args, **kwargs)