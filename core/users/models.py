from django.db import models

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True , default='avatars/default.jpg')

    def __str__(self):

        return self.user.username



