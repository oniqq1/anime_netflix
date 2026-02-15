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


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    anime = models.ForeignKey(AnimeDescription, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.anime.name}"