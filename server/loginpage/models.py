from django.db import models

# Create your models here.
class user_login(models.Model):
    username = models.TextField()
    email = models.TextField()
    password = models.TextField()