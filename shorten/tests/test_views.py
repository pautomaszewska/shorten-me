from django.test import TestCase
from shorten.models import URL


class TestURLViews(TestCase):
    def setUp(self):
        test_url = URL.objects.create(long_url='https://github.com/pautomaszewska?tab=repositories')
        test_url.save()

    def test_get_short_url(self):
        url = URL.objects.get(long_url='https://github.com/pautomaszewska?tab=repositories')
        url_data = {
            "long_url": "{}".format(url.long_url),
            "short_url": "{}".format(url.short_url)
        }
        response = self.client.post('/', url_data)
        self.assertEqual(response.status_code, 200)

    def test_create_short_ulr(self):
        new_url = {
            "long_url": "https://www.youtube.com/watch?v=3PwF81bPvKg",
        }
        response = self.client.post('/', new_url)
        self.assertEqual(response.status_code, 200)

    def test_url_redirect(self):
        url = URL.objects.get(long_url='https://github.com/pautomaszewska?tab=repositories')
        short_url = url.short_url

        response = self.client.get('/{}'.format(short_url))
        self.assertEqual(response.status_code, 302)
