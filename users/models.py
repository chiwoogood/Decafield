from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=11, blank=True, null=True)
    nickname = models.CharField(max_length=9, blank=True, null=True)
    email = models.EmailField(unique=True, blank=True, null=True)
    coffee_type = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.username