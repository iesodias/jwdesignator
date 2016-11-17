from django.test import TestCase
from designator.groups.models import Group

class GroupModelTest(TestCase):
    def setUp(self):
        self.obj = Group(
            name = 'Ieso Dias',
            address = 'Rua Modestino',
            sup_group = 'Ieso'
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Group.objects.exists())

    def test_str(self):
        self.assertEqual('Ieso Dias', str(self.obj))