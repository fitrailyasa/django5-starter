from django.shortcuts import render, get_object_or_404, redirect
from django.core.files.storage import FileSystemStorage
from product.models import Product
from category.models import Category
from .forms import productCreateForm, productEditForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def index_product(request):
    all_categories = Category.objects.all()
    all_products = Product.objects.all()
    context = {'title': 'Product', 'products': all_products, 'categories': all_categories}
    return render(request, 'product/index.html', context)

@login_required
def create_product(request):
    if request.method == 'POST':
        form = productCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product has been created.')
            return redirect('index_product')
        else:
            messages.error(request, 'Product failed to create.')
    else:
        form = productCreateForm()
    
    context = {'form': form}
    return render(request, 'product/create.html', context)

@login_required
def update_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        form = productEditForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product has been updated.')
            return redirect('index_product')
        else:
            messages.error(request, 'Product failed to update.')
    else:
        form = productEditForm(instance=product)

    context = {'form': form, 'product': product}
    return render(request, 'product/edit.html', context)

@login_required
def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Product has been deleted.')
        return redirect('index_product')
    else:
        messages.error(request, 'Product failed to delete.')

    context = {'product': product}
    return render(request, 'product/delete.html', context)
