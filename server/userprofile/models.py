from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class user_profile(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.TextField()
    email = models.TextField()

    def __str__(self):
        return self.user.username
    