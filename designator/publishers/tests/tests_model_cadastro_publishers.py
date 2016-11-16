from django.test import TestCase
from designator.publishers.models import Publisher

class PublishersCadastroTest(TestCase):
    def setUp(self):
        self.obj = Publisher(
            name='Ieso',
            address='Rua Italia',
            phone='31985697523',
            email='teste@gmail.com',
            gender='Masculino',
            designation='Teste',
            group='Make a Queryset',
            car='Sim'
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Publisher.objects.exists())

    def test_str(self):
        self.assertEqual('Ieso', str(self.obj))