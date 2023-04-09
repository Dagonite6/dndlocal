from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Character(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    experience = models.PositiveIntegerField(default=0)
    race = models.PositiveSmallIntegerField()
    char_class = models.PositiveSmallIntegerField()
    stats = ArrayField(models.PositiveSmallIntegerField(), size=6)
    spells = ArrayField(models.PositiveSmallIntegerField(), default=0)
    items = ArrayField(models.PositiveSmallIntegerField(), default=0)

class CharacterParams(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    param_name = models.CharField(max_length=50)
    param_value = models.CharField(max_length=200)


