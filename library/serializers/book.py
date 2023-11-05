from rest_framework import serializers
from library.models.book import Book
from library.models.author import Author


class BookSerializer(serializers.ModelSerializer):
    authors = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all(), many=True)

    class Meta:
        model = Book
        fields = ('id', 'name', 'edition', 'publication_year', 'authors')

