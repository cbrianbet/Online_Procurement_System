from django.db import models


# Create your models here.
class User(models.Model):
    userName = models.CharField(max_length=64)
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    companyName = models.CharField(max_length=64)
    role = models.CharField(max_length=20)
