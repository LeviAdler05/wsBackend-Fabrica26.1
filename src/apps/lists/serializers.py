from rest_framework import serializers
from .models import Favorite, List, ListItem
from apps.characters.serializers import CharacterSerializer


class FavoriteSerializer(serializers.ModelSerializer):
    character = CharacterSerializer(read_only=True)

    class Meta:
        model = Favorite
        fields = '__all__'
        read_only_fields = ['user']


class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = '__all__'
        read_only_fields = ['user']


class ListItemSerializer(serializers.ModelSerializer):
    character = CharacterSerializer(read_only=True)

    class Meta:
        model = ListItem
        fields = '__all__'

class AddCharacterSerializer(serializers.Serializer):
    api_id = serializers.IntegerField()