import csv
from django.core.management.base import BaseCommand
from library.models.author import Author

class Command(BaseCommand):
    help = 'Import authors from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')

    def handle(self, *args, **options):
        csv_file_path = options['csv_file']

        with open(csv_file_path, 'r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                author_name = row.get('name')
                if author_name:
                    author, created = Author.objects.get_or_create(name=author_name)
                    if created:
                        self.stdout.write(self.style.SUCCESS(f'Author "{author_name}" imported successfully.'))
                    else:
                        self.stdout.write(self.style.WARNING(f'Author "{author_name}" already exists.'))
