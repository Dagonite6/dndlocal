from rest_framework import serializers
from . models import Race

class RaceListSerializer(serializers.ModelSerializer):   
    class Meta:
        model = Race
        fields = ('id', 'en_name', 'ru_name')