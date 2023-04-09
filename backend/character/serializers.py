from rest_framework import serializers
from . models import Character
from . import constants

#на беке мне кажется лучше чекать только в нужном ли формате статы, что бы не огрничивать себя в будущем
#то что они больше чем технически возможно по уровню лучше выкидывать в алерт на фронте. С кнопкой что да, это намерено, если юзер так хочет
#чек на то инт ли это ИнтФилд в сериалайзере делает сам
def stats_validator(stats):
    for stat in stats:
        if stat <=0 :
            raise serializers.ValidationError({"stats": "Stats can't be negative or zero"})
        
def race_validator(race):
    if race > constants.MAX_RACE:
        raise serializers.ValidationError({"race": "Race overflow."})
    
def class_validator(char_class):
    if char_class > constants.MAX_CLASS:
            raise serializers.ValidationError({"class": "Class overflow."})

class CharacterSerializer(serializers.ModelSerializer):
    char_class = serializers.IntegerField(validators=[class_validator])
    race = serializers.IntegerField(validators=[race_validator])   
    stats = serializers.ListField(child=serializers.IntegerField(), validators=[stats_validator])
    class Meta:
        model = Character
        fields = '__all__'

class ListSerializer(serializers.ModelSerializer):   
    class Meta:
        model = Character
        fields = ('id', 'name', 'experience', 'race', 'char_class')

class CreateSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    char_class = serializers.IntegerField(required=True, validators=[class_validator])
    race = serializers.IntegerField(required=True, validators=[race_validator])
    stats = serializers.ListField(child=serializers.IntegerField(), required=True, validators=[stats_validator])
    spells = serializers.ListField(child=serializers.IntegerField())
    items = serializers.ListField(child=serializers.IntegerField())

    class Meta:
        model = Character
        fields = ('id', 'name', 'race', 'char_class', 'stats', 'spells', 'items')

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