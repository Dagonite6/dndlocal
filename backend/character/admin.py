from django.contrib import admin

# Register your models here.
from .models import Character, CharacterParams

admin.site.register(Character)
admin.site.register(CharacterParams)
