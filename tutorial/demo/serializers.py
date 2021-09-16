from rest_framework import serializers
from .models import Book, ISBN, Character,Author


class ISBNSerializer(serializers.ModelSerializer):
    class Meta:
        model = ISBN
        fields = '__all__'


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = '__all__'



class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id','first_name','last_name']


class BookSerializer(serializers.ModelSerializer):
    ISBN = ISBNSerializer(many=False)
    characters = CharacterSerializer(many=True)
    authors = AuthorSerializer(many=True)
    class Meta:
        model = Book
        fields = '__all__'
