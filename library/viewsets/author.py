from rest_framework import viewsets
from library.models.author import Author
from library.serializers.author import AuthorSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


