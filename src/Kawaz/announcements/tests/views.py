# -*- coding: utf-8 -*-
#
# updated:        2010/11/16
# Author:        alisue
#
from django.conf import settings
from django.test import TestCase
from django.contrib.auth.models import Permission

from qwert.tests.userset import Userset
from ..models import Announcement

import os.path

class AnnouncementViewTest(TestCase):
    urls = 'Kawaz.announcements.tests.urls'
    fixtures = ['test_data.yaml']
    template_dirs = (
        os.path.join(os.path.dirname(__file__), '../templates'),
    )
    
    def setUp(self):
        self.template_dirs_backup = settings.TEMPLATE_DIRS
        settings.TEMPLATE_DIRS = self.template_dirs
        # update access userset
        self.userset = Userset()
        self.userset.staff.user_permissions.add(Permission.objects.get_by_natural_key('add_announcement', 'announcements', 'announcement'))
        self.userset.staff.user_permissions.add(Permission.objects.get_by_natural_key('change_announcement', 'announcements', 'announcement'))
        self.userset.staff.user_permissions.add(Permission.objects.get_by_natural_key('delete_announcement', 'announcements', 'announcement'))
        self.userset.staff.save()
        # update dummy data
        self.dummy = {'pub_state': 'public', 'title': 'foobar', 'body': 'hogehoge', 'sage': False}
        
    def tearDown(self):
        settings.TEMPLATE_DIRS = self.template_dirs_backup
        
    def test_list_view(self):
        response = self.client.get("")
        self.assertEqual(response.status_code, 200)
    
    def test_detail_view(self):
        response = self.client.get("/1/")
        self.assertEqual(response.status_code, 200)
    def test_invalid_detail_view(self):
        response = self.client.get("/A/")
        self.assertEqual(response.status_code, 404)
        
    def test_archive_year_view(self):
        response = self.client.get("/archive/2010/")
        self.assertEqual(response.status_code, 200)
    def test_archive_month_view(self):
        for month in xrange(1, 12):
            response = self.client.get("/archive/2010/%d/" % month)
            self.assertEqual(response.status_code, 200)
    
    def test_create_view_guest(self):
        response = self.client.get("/create/")
        self.assertEqual(response.status_code, 302)
        response = self.client.post("/create/", self.dummy)
        self.assertEqual(response.status_code, 302)
    def test_create_view_user(self):
        self.assertEqual(self.userset.login_user(self.client), True)
        response = self.client.get("/create/")
        self.assertEqual(response.status_code, 403)
        response = self.client.post("/create/", self.dummy)
        self.assertEqual(response.status_code, 403)
    def test_create_view_staff(self):
        self.assertEqual(self.userset.login_staff(self.client), True)
        response = self.client.get("/create/")
        self.assertEqual(response.status_code, 200)
        response = self.client.post("/create/", self.dummy)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Announcement.objects.filter(title="foobar").exists(), True)
    def test_create_view_superuser(self):
        self.assertEqual(self.userset.login_admin(self.client), True)
        response = self.client.get("/create/")
        self.assertEqual(response.status_code, 200)
        response = self.client.post("/create/", self.dummy)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Announcement.objects.filter(title="foobar").exists(), True)
    
    def test_update_view_guest(self):
        response = self.client.get("/1/update/")
        self.assertEqual(response.status_code, 302)
        response = self.client.post("/1/update/", self.dummy)
        self.assertEqual(response.status_code, 302)
    def test_update_view_user(self):
        self.assertEqual(self.userset.login_user(self.client), True)
        response = self.client.get("/1/update/")
        self.assertEqual(response.status_code, 403)
        response = self.client.post("/1/update/", self.dummy)
        self.assertEqual(response.status_code, 403)
    def test_update_view_staff(self):
        self.assertEqual(self.userset.login_staff(self.client), True)
        response = self.client.get("/1/update/")
        self.assertEqual(response.status_code, 200)
        response = self.client.post("/1/update/", self.dummy)
        print response
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Announcement.objects.filter(title="foobar").exists(), True)
    def test_update_view_superuser(self):
        self.assertEqual(self.userset.login_admin(self.client), True)
        response = self.client.get("/1/update/")
        self.assertEqual(response.status_code, 200)
        response = self.client.post("/1/update/", self.dummy)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Announcement.objects.filter(title="foobar").exists(), True)

    def test_delete_view_guest(self):
        response = self.client.get("/1/delete/")
        self.assertEqual(response.status_code, 302)
        response = self.client.post("/1/delete/")
        self.assertEqual(response.status_code, 302)
    def test_delete_view_user(self):
        self.assertEqual(self.userset.login_user(self.client), True)
        response = self.client.get("/1/delete/")
        self.assertEqual(response.status_code, 403)
        response = self.client.post("/1/delete/")
        self.assertEqual(response.status_code, 403)
    def test_delete_view_staff(self):
        self.assertEqual(self.userset.login_staff(self.client), True)
        last_count = Announcement.objects.count()
        response = self.client.get("/1/delete/")
        self.assertEqual(response.status_code, 200)
        response = self.client.post("/1/delete/")
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Announcement.objects.count(), last_count - 1)
    def test_delete_view_superuser(self):
        self.assertEqual(self.userset.login_admin(self.client), True)
        last_count = Announcement.objects.count()
        response = self.client.get("/1/delete/")
        self.assertEqual(response.status_code, 200)
        response = self.client.post("/1/delete/")
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Announcement.objects.count(), last_count - 1)