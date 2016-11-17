from django.test import TestCase
from designator.groups.models import Group

class Group_Post_Valid(TestCase):
    def test_save_group(self):
        self.assertTrue(Group.objects.exists())

class Group_Post_Invalid(TestCase):
    def test_dont_save_group(self):
        self.assertFalse(Group.objects.exists())