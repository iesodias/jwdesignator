from django.test import TestCase
from designator.publishers.models import Publisher

class PublishersCadastroTest(TestCase):
    def test_create(self):
        obj = Publisher(
            name='Ieso Dias',
            address='Rua Modestino Eloy',
            phone='31992323628',
            email='iesodias@gmail.com',
            gender='Masculino',
            designation='Ancião',
            group='Make a Queryset',
            car='Sim'
        )
        obj.save()
        self.assertTrue(Publisher.objects.exists())