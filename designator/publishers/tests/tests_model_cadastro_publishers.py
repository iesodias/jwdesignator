from django.test import TestCase
from designator.publishers.models import Publisher

class PublishersCadastroTest(TestCase):
    def test_create(self):
        obj = Publisher(
            name='Ieso Dias',
            address='Rua Italia',
            phone='31985697523',
            email='teste@gmail.com',
            gender='Masculino',
            designation='Teste',
            group='Make a Queryset',
            car='Sim'
        )
        obj.save()
        self.assertTrue(Publisher.objects.exists())