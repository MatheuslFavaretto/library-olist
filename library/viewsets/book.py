from rest_framework import viewsets
from library.models.book import Book
from library.serializers.book import BookSerializer
from django_filters import rest_framework as django_filters


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookFilter(django_filters.FilterSet):
    class Meta:
        model = Book
        fields = {
            'name': ['icontains'],
            'publication_year': ['exact'],
            'edition': ['exact'],
            'authors__name': ['icontains'],
        }

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filterset_class = BookFilter
