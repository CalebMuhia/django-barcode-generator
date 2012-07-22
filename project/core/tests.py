# pylint: disable-msg=R0904


from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse


class HomeTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('core:home')

    def test_url(self):
        self.assertEqual(self.url, '/')

    def test_status_code(self):
        response = self.client.get(self.url)
        self.assertContains(response, 'It works Jim!')
