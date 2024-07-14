from django.core.management.base import BaseCommand
from product.models import Product
from category.models import Category

class Command(BaseCommand):
    help = 'Seed products for initial data'

    def handle(self, *args, **kwargs):
        products_data = [
            {'name': 'Product 1', 'price': 1000, 'desc': 'Description for product 1', 'category_id': 1},
            {'name': 'Product 2', 'price': 1000, 'desc': 'Description for product 2', 'category_id': 2},
            {'name': 'Product 3', 'price': 1000, 'desc': 'Description for product 3', 'category_id': 3},
        ]
        
        for product_data in products_data:
            category_id = product_data.pop('category_id')  # Remove category_id from product_data
            try:
                category = Category.objects.get(id=category_id)  # Fetch the Category instance
                product_data['category_id'] = category  # Add the Category instance back to product_data
                if not Product.objects.filter(name=product_data['name']).exists():
                    Product.objects.create(**product_data)
                    self.stdout.write(self.style.SUCCESS(f"Product '{product_data['name']}' created successfully"))
                else:
                    self.stdout.write(self.style.WARNING(f"Product '{product_data['name']}' already exists"))
            except Category.DoesNotExist:
                self.stdout.write(self.style.ERROR(f"Category with id {category_id} does not exist"))