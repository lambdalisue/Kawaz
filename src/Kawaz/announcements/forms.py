# -*- coding: utf-8 -*-
from django import forms
from models import Announcement

class AnnouncementForm(forms.ModelForm):
    class Meta:
        model   = Announcement
        fields  = ('pub_state', 'title', 'body', 'sage')