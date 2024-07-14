from django.urls import path
from .views import *

urlpatterns = [
    path('', index_category, name='index_category'),
    path('create/', create_category, name='create_category'),
    path('<int:category_id>/', update_category, name='update_category'),
    path('<int:category_id>/delete/', delete_category, name='delete_category'),
]