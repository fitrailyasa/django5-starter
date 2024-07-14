from django.urls import path
from .views import *

urlpatterns = [
    path('', index_user, name='index_user'),
    path('create/', create_user, name='create_user'),
    path('<int:user_id>/', update_user, name='update_user'),
    path('<int:user_id>/delete/', delete_user, name='delete_user'),
]