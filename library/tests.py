from django.test import TestCase
from library.models.book import Book
from library.models.author import Author


## Author TestCase
class AuthorModelTest(TestCase):

    def setUp(self):
        self.author = Author.objects.create(name='Autor de Teste')

    def test_author_creation(self):
        author = Author.objects.get(id=1)
        self.assertEqual(author.name, 'Autor de Teste')

    def test_author_str_representation(self):
        author = Author.objects.get(id=1)
        self.assertEqual(str(author), 'Autor de Teste')


## Book TestCase
class BookModelTest(TestCase):

    def test_book_creation(self):
        author = Author.objects.create(name='Autor de Teste')
        book = Book.objects.create(
            name='Livro de Teste',
            edition=1,
            publication_year=2023
        )
        book.authors.add(author)

        self.assertEqual(book.name, 'Livro de Teste')
        self.assertEqual(book.edition, 1)
        self.assertEqual(book.publication_year, 2023)
        self.assertEqual(book.authors.count(), 1)
        self.assertEqual(book.authors.first().name, 'Autor de Teste')

    def test_book_str_representation(self):
        author = Author.objects.create(name='Autor de Teste')
        book = Book.objects.create(
            name='Livro de Teste',
            edition=1,
            publication_year=2023
        )
        book.authors.add(author)

        self.assertEqual(str(book), 'Livro de Teste')

