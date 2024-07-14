from django.shortcuts import render, get_object_or_404, redirect
from category.models import Category
from .forms import categoryCreateForm, categoryEditForm
from django.contrib import messages

def index_category(request):
    all_categories = Category.objects.all()
    context = {'categories': all_categories}
    return render(request, 'category/index.html', context)

def create_category(request):
    if request.method == 'POST':
        form = categoryCreateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category berhasil dibuat.')
            return redirect('index_category')
        else:
            messages.error(request, 'Terjadi kesalahan saat membuat category.')
    else:
        form = categoryCreateForm()
    
    context = {'form': form}
    return render(request, 'category/create.html', context)

def update_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)

    if request.method == 'POST':
        form = categoryEditForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category berhasil diperbarui.')
            return redirect('index_category')
        else:
            messages.error(request, 'Terjadi kesalahan saat memperbarui category.')
    else:
        form = categoryEditForm(instance=category)

    context = {'form': form, 'category': category}
    return render(request, 'category/edit.html', context)

def delete_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)

    if request.method == 'POST':
        category.delete()
        messages.success(request, 'Category berhasil dihapus.')
        return redirect('index_category')
    else:
        messages.error(request, 'Terjadi kesalahan saat menghapus category.')

    context = {'category': category}
    return render(request, 'category/delete.html', context)
