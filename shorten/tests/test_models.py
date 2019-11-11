from django.test import TestCase
from shorten.models import URL


class URLTest(TestCase):
    def setUp(self):
        test_url = URL.objects.create(long_url='https://github.com/pautomaszewska?tab=repositories')
        test_url.save()

    def test_short_url(self):
        url = URL.objects.get(id=1)
        expected_short_url = 'MQ=='
        self.assertEquals(url.short_url, expected_short_url)
