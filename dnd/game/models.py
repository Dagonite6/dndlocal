from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} Profile'

class Character(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    race = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    level = models.PositiveSmallIntegerField()
    history = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    summoner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    