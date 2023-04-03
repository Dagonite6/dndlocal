from rest_framework import serializers
from . models import Character
from . import constants

class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        field = ('id', 'name', 'experience', 'race', 'char_class', 'stats', 'spells', 'items')

class ListSerializer(serializers.Serializer):
    def validate(self, data):
        print(data) 
        raise serializers.ValidationError({"Message": "shit"})
    
    class Meta:
        model = Character
        fields = ('id', 'name', 'experience', 'race', 'char_class', 'stats', 'spells', 'items')

class CreateSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    char_class = serializers.IntegerField(required=True)
    race = serializers.IntegerField(required=True)
    stats = serializers.ListField(child=serializers.IntegerField(), required=True)
    spells = serializers.ListField(child=serializers.IntegerField(), required=True)
    items = serializers.ListField(child=serializers.IntegerField(), required=True)

    class Meta:
        model = Character
        fields = ('id', 'name', 'race', 'char_class', 'stats', 'spells', 'items')

    def validate(self, attrs):
        if sum(attrs['stats']) > constants.MAX_STATS:
            raise serializers.ValidationError({"stats": "Stats overflow."})
        if attrs['race'] > constants.MAX_RACE:
            raise serializers.ValidationError({"race": "Race overflow."})
        if attrs['char_class'] > constants.MAX_CLASS:
            raise serializers.ValidationError({"class": "Class overflow."})

        return attrs

    def create(self, validated_data):
        character = Character.objects.create(
            name=validated_data["name"],
            user_id=self.context['request'].user.id,
            char_class=validated_data['char_class'],
            race=validated_data["race"],
            stats=validated_data["stats"],
            spells=validated_data["spells"],
            items=validated_data["items"],
        )
    
        character.save()
        return character