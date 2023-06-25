from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    bio = models.CharField('bio', max_length=255)
    image = models.ImageField('image', upload_to='media/profile_images/', null=True, blank=True)