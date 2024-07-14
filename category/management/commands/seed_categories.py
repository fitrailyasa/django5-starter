from django.core.management.base import BaseCommand
from category.models import Category

class Command(BaseCommand):
    help = 'Seed categories for initial data'

    def handle(self, *args, **kwargs):
        categories_data = [
            {'name': 'Category 1', 'desc': 'Description for category 1'},
            {'name': 'Category 2', 'desc': 'Description for category 2'},
            {'name': 'Category 3', 'desc': 'Description for category 3'},
        ]
        
        for category_data in categories_data:
            if not Category.objects.filter(name=category_data['name']).exists():
                Category.objects.create(**category_data)
                self.stdout.write(self.style.SUCCESS(f"Category '{category_data['name']}' created successfully"))
            else:
                self.stdout.write(self.style.WARNING(f"Category '{category_data['name']}' already exists"))