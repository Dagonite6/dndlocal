from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

def get_default_array():
    return []

class Character(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    experience = models.PositiveIntegerField(default=0)
    race = models.PositiveSmallIntegerField(default=0)
    char_class = models.PositiveSmallIntegerField(default=0)
    stats = ArrayField(models.PositiveSmallIntegerField(), size=6)
    spells = ArrayField(models.PositiveSmallIntegerField(), default=get_default_array)
    items = ArrayField(models.PositiveSmallIntegerField(), default=get_default_array)

    def save(self,*args,**kwargs):
        created = not self.pk
        super().save(*args,**kwargs)
        if created:
            CharacterParams.objects.create(user=self)

class CharacterParams(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    param_name = models.CharField(max_length=50)
    param_value = models.TextField()




