from django.contrib import admin
from django.urls import path
from . import controller, views


urlpatterns = [
    path('', controller.index),
    path('character/', views.CharacterListCreate.as_view())
]
