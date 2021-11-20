from django.db import models


class Link(models.Model):
    url = models.URLField()
    tiny_url = models.URLField()
    token = models.CharField(max_length=16)

    def __str__(self):
        return self.url
