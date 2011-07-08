#!/usr/bin/env python
# vim: set fileencoding=utf8 :
"""Local settings module

This module never shared via Github. So use this module
to configure secret data like Password or whatever.


Copyright:
    Copyright 2011 Alisue allright reserved.

License:
    Licensed under the Apache License, Version 2.0 (the "License"); 
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unliss required by applicable law or agreed to in writing, software
    distributed under the License is distrubuted on an "AS IS" BASICS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""
__author__  = 'Alisue <lambdalisue@hashnote.net>'
__version__ = '1.0.0'
__date__    = '2011/07/08'
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User as _User

class OAuth(models.Model):
    consumer = models.CharField("Consumer", max_length=50)
    access_token = models.CharField("Access token", max_length=256)

    def __init__(self):
        pass
    
class User(_User):
    oauth = models.ForeignKey('OAuth', verbose_name="OAuth", null=True, blank=True, editable=False)
    
    @property
    def is_guest(self):
        return self.oauth is not None

# Automatically create user account for OAuth
def oauth_post_save_callback(sender, instance, created, *args, **kwargs):
    if created:
        pass
    


    