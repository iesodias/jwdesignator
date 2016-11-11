from django.test import TestCase
from designator.publishers.models import Publisher


class Cadastro_Post_Valid(TestCase):
    def test_save_cadastro_publish(self):
        self.assertTrue(Publisher.objects.exists())


class Cadastro_Post_Invalid(TestCase):
    def test_dont_save_publisher(self):
        self.assertFalse(Publisher.objects.exists())