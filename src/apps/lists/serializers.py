from rest_framework import serializers
from .models import Favorite, List, ListItem


class FavoriteSerializer(serializers.ModelSerializer):
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
    class Meta:
        model = ListItem
        fields = '__all__'