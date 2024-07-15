from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class Command(BaseCommand):
    help = 'Seed users for initial data'

    def handle(self, *args, **kwargs):
        users_data = [
            {'username': 'admin1', 'email': 'admin1@admin.com', 'password': 'password1'},
            {'username': 'admin2', 'email': 'admin2@admin.com', 'password': 'password2'},
            {'username': 'admin3', 'email': 'admin3@admin.com', 'password': 'password3'},
        ]
        
        for user_data in users_data:
            username = user_data['username']
            if not User.objects.filter(username=username).exists():
                password = make_password(user_data['password'])
                User.objects.create(username=username, email=user_data['email'], password=password)
                self.stdout.write(self.style.SUCCESS(f"User '{username}' created successfully"))
            else:
                self.stdout.write(self.style.WARNING(f"User '{username}' already exists"))
