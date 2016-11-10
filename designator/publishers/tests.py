from django.test import TestCase
from designator.publishers.forms import PublisherForm

class SubscribePublishers(TestCase):
    def setUp(self):
        self.resp = self.client.get('/cadastro/')

    """get /publishers/ must return status 200"""
    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'publishers/cadastro_form.html')

    def test_html(self):
        """HTML must contain inputs tags"""
        self.assertContains(self.resp, '<form')
        self.assertContains(self.resp, '<input', 6)
        self.assertContains(self.resp, 'type="text"', 3)
        self.assertContains(self.resp, 'type="email"')
        self.assertContains(self.resp, 'type="submit"')

    def test_csrf(self):
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def test_has_form(self):
        form = self.resp.context['form']
        self.assertIsInstance(form, PublisherForm)

    def test_form_has_fields(self):
        form = self.resp.context['form']
        self.assertSequenceEqual(['name','address','phone','email','gender','designation','group','car'], list(form.fields))