from django.db import models

# Create your models here.
class Race (models.Model):
    en_name = models.CharField(max_length=100)
    ru_name = models.CharField(max_length=100)
