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
from django.http import HttpResponseRedirect
import oauth2 as oauth
import urllib

from models import OAuth

class OAuthBackend(object):
    label = None
    request_token_url = None
    access_token_url = None
    authorize_url = None
    
    callback_url = None
    
    def __init__(self, consumer_key, consumer_secret):
        self.consumer = oauth.Consumer(key=consumer_key, secret=consumer_secret)
    
    def get_request_token_url(self):
        return self.request_token_url
    def get_authorize_url(self):
        return self.authorize_url
    def get_access_token_url(self):
        return self.access_token_url
    def get_callback_url(self):
        return self.callback_url

    
    def index(self, request):
        client = oauth.Client(self.consumer)
        response, content = client.request(
            self.get_request_token_url(),
            'POST',
            body=urllib.urlencode({
                'oauth_callback': self.get_callback_url(),
            }),
        )
        request_token = {}

        request_token = {}
        for item in content.split('&'):
            _data = item.split('=')
            request_token.update({_data[0]: _data[1]})
    
        request.session['request_token'] = request_token
        redirect_url = "%s?oauth_token=%s" % (self.get_authorize_url(), request_token['oauth_token'])
        return HttpResponseRedirect(redirect_url)

    def callback(self, request):
        request_token = request.session['request_token']
        token = oauth.Token(
            request_token['oauth_token'],
            request_token['oauth_token_secret']
        )
        client = oauth.Client(self.consumer, token)
    
        _dict = {
            'oauth_token': request.GET['oauth_token'],
            'oauth_verifier': request.GET['oauth_verifier'],
        }
    
        response, content = client.request(
            self.get_access_token_url(),
            "POST",
            body=urllib.urlencode(_dict)
        )
    
        access_token = {}
        for item in content.split('&'):
            _data = item.split('=')
            access_token.update({_data[0]: _data[1]})
    
        OAuth.objects.get_or_create(consumer=self.label, access_token=access_token)
        request.session['access_token'] = access_token
    
        return HttpResponseRedirect('/timeline/')

def timeline(request):

    access_token = request.session['access_token']

    token = oauth.Token(access_token['oauth_token'],
            access_token['oauth_token_secret'])
    client = oauth.Client(consumer, token)
    _result = client.request(timeline_url, 'GET')

    _statuses = _result[1]
    xmlString = urllib.unquote_plus(_statuses.encode('utf-8'))
    elem = fromstring(xmlString)
    for element in elem.findall("status"):
        print element.find('text').text

    return render_to_response('index.html')