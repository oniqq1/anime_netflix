from django.contrib.auth.models import User
from django.db import models


class Comment(models.Model):
    author = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE)
    comment_content = models.TextField(max_length="455")
    created_at = models.DateTimeField(auto_now_add=True)

    # Крутая штука кстати
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.author.username
