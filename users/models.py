from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    email = models.EmailField()
    membership_date = models.DateTimeField(auto_now_add=True)

# class Member(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField()
#     membership_date = models.DateTimeField()