from django.db import models


class Link(models.Model):
    url = models.URLField()
    tiny_url = models.URLField()

    def __str__(self):
        return self.url
