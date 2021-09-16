from rest_framework import serializers
from .models import Book, ISBN, Character


class ISBNSerializer(serializers.ModelSerializer):
    class Meta:
        model = ISBN
        fields = '__all__'


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    ISBN = ISBNSerializer(many=False)
    characters = CharacterSerializer(many=True)

    class Meta:
        model = Book
        fields = '__all__'
