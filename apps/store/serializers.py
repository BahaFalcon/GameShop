from rest_framework import serializers

from .models import Game, Genre


class GameSerializer(serializers.ModelSerializer):
    price = serializers.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        model = Game
        fields = ('id', 'name', 'genre', 'image', 'description', 'price', 'available',)


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'title',)