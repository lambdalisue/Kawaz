# -*- coding: utf-8 -*-
#
# Author:        alisue
# Date:            2010/11/12
#
from django.test import TestCase
from django.db import IntegrityError
from django.contrib.auth.models import User
from ..models import Announcement

class AnnouncementModelTest(TestCase):
    fixtures = ['test_data.yaml']
    
    def setUp(self):
        self.admin = User.objects.get(pk=1)
    
    def _create_announcement(self):
        new_obj = Announcement.objects.create(
            title='foobar',
            body='hogehoge',
            sage=True,
            author=self.admin,
            updated_by=self.admin,
        )
        return new_obj
    def test_create_model(self):
        new_obj = self._create_announcement()
        self.assertTrue(Announcement.objects.filter(title='foobar').exists())
        found_obj = Announcement.objects.get(title='foobar')
        self.assertEqual(new_obj, found_obj)
    
    def test_create_invalid_model(self):
        self.assertRaises(IntegrityError, Announcement.objects.create, 
            title=None,
            body='body',
            sage=True,
            author=self.admin,
            updated_by=self.admin,
        )
        self.assertRaises(IntegrityError, Announcement.objects.create,
            pk = 1,
            title='foobar',
            body='hogehoge',
            sage=True,
            author=self.admin,
            updated_by=self.admin,
        )
    
    def test_update_model(self):
        self._create_announcement()
        found_obj = Announcement.objects.get(title='foobar')
        found_obj.title = 'AAAAA'
        found_obj.body = 'BBBBB'
        found_obj.sage = False
        found_obj.save()
        self.assertTrue(Announcement.objects.filter(title='AAAAA').exists())
        found_obj2 = Announcement.objects.get(title='AAAAA')
        self.assertEqual(found_obj, found_obj2)
    
    def test_update_invalid_model(self):
        self._create_announcement()
        found_obj = Announcement.objects.get(title='foobar')
        found_obj.title = None
        self.assertRaises(IntegrityError, found_obj.save)
        
    def test_delete_model(self):
        self._create_announcement()
        found_obj = Announcement.objects.get(title='foobar')
        found_obj.delete()
        self.assertTrue(not Announcement.objects.filter(title='foobar').exists())