from django.db import models
from datetime import date
# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    birthday = models.DateField(null=True, blank=True, default=date.today)