from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from category.models import Category
from product.models import Product
from django.contrib.auth.models import User

@login_required
def dashboard(request):
    # count semua model
    category_count = Category.objects.count()
    product_count = Product.objects.count()
    user_count = User.objects.count()
    context = {
        'title': 'Dashboard',
        'category_count': category_count,
        'product_count': product_count,
        'user_count': user_count,
        'other_count': 0
    }
    return render(request, 'dashboard.html', context)
