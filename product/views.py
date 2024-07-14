from django.shortcuts import render, get_object_or_404, redirect
from django.core.files.storage import FileSystemStorage
from product.models import Product
from category.models import Category
from .forms import productCreateForm, productEditForm
from django.contrib import messages

def index_product(request):
    all_categories = Category.objects.all()
    all_products = Product.objects.all()
    context = {'products': all_products, 'categories': all_categories}
    return render(request, 'product/index.html', context)

def create_product(request):
    if request.method == 'POST':
        form = productCreateForm(request.POST, request.FILES)  # Handle file uploads
        if form.is_valid():
            form.save()
            messages.success(request, 'Product berhasil dibuat.')
            return redirect('index_product')
        else:
            messages.error(request, 'Terjadi kesalahan saat membuat product.')
    else:
        form = productCreateForm()
    
    context = {'form': form}
    return render(request, 'product/create.html', context)

def update_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        form = productEditForm(request.POST, request.FILES, instance=product)  # Handle file uploads
        if form.is_valid():
            form.save()
            messages.success(request, 'Product berhasil diperbarui.')
            return redirect('index_product')
        else:
            messages.error(request, 'Terjadi kesalahan saat memperbarui product.')
    else:
        form = productEditForm(instance=product)

    context = {'form': form, 'product': product}
    return render(request, 'product/edit.html', context)

def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Product berhasil dihapus.')
        return redirect('index_product')
    else:
        messages.error(request, 'Terjadi kesalahan saat menghapus product.')

    context = {'product': product}
    return render(request, 'product/delete.html', context)
