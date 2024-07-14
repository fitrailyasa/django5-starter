from django.urls import path
from .views import *

urlpatterns = [
    path('', index_product, name='index_product'),
    path('create/', create_product, name='create_product'),
    path('<int:product_id>/', update_product, name='update_product'),
    path('<int:product_id>/delete/', delete_product, name='delete_product'),
]