from django.contrib.auth.models import User
from django.db import models


class AnimeDescription(models.Model):
    name = models.CharField(max_length=255, unique=True)
    appearing = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    genres = models.CharField(max_length=500)
    description = models.TextField()
    poster = models.ImageField(upload_to="posters/", blank=True, default="")

    def __str__(self):
        return self.name


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="anime_comments")
    anime = models.ForeignKey(AnimeDescription, on_delete=models.CASCADE, related_name="comments")
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.user.username} - {self.anime.name}"