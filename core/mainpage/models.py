from django.contrib.auth.models import User
from django.db import models


class AnimeDescription(models.Model):
    name = models.CharField()
    appearing = models.TextField()
    type = models.TextField()
    genres = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.name