from django.db import models
from shortener import settings
import base64


class URL(models.Model):
    long_url = models.URLField(verbose_name='')
    short_url = models.URLField()

    def save(self, *args, **kwargs):
        url_id = str(self.id)
        encoded_url = base64.b64encode(url_id.encode("utf-8"))
        shortened = (str(encoded_url, "utf-8"))
        self.short_url = shortened

        super(URL, self).save(*args, **kwargs)

    def show_whole_link(self):
        return settings.SITE_URL + self.short_url

    def __str__(self):
        return self.show_whole_link()
