from django.db import models
from library.models.author import Author


class Book(models.Model):
    name = models.CharField(max_length=255)
    edition = models.IntegerField()
    publication_year = models.IntegerField()
    authors = models.ManyToManyField(Author)

    def __str__(self):
        return self.name
    