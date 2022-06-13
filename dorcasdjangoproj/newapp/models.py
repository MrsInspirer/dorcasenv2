from unicodedata import name
from django.db import models

# Create your models here.
class  DorcasOfem(models.Model):
    name = models.CharField(max_length= 23)
