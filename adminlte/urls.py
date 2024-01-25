from django.urls import path
from .views import dashboard, index_user, create_user, update_user, delete_user

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('dashboard/', dashboard, name='dashboard'),
    path('user/', index_user, name='index_user'),
    path('user/create/', create_user, name='create_user'),
    path('user/<int:user_id>/', update_user, name='update_user'),
    path('user/<int:user_id>/delete/', delete_user, name='delete_user'),
]

# app_name = 'adminlte'