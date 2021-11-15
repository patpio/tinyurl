from uuid import uuid4

from django.contrib.sites.models import Site
from django.db import models


class Link(models.Model):
    url = models.URLField()
    tiny_url = models.URLField()

    def save(self, *args, **kwargs):
        domain = Site.objects.get_current().domain
        token = uuid4()
        self.tiny_url = f'http://{domain}{token}'

        return super().save(*args, **kwargs)

    def __str__(self):
        return self.url
