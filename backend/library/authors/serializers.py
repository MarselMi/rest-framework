from rest_framework import serializers
from .models import Author, Article, Book, Biography


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class BiographySerializer(serializers.ModelSerializer):
    class Meta:
        model = Biography
        fields = ['text', 'author']


class ArticleSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    class Meta:
        model = Article
        exclude = ['name']


class BookSerializer(serializers.ModelSerializer):
    authors = serializers.StringRelatedField(many=True)
    class Meta:
        model = Book
        fields = '__all__'