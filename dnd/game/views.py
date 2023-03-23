from django.shortcuts import render

# Create your views here.
from .models import Character
from .serializers import CharacterSerializer
from rest_framework import generics

class CharacterListCreate(generics.ListCreateAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer