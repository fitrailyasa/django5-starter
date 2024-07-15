from django.shortcuts import render, get_object_or_404, redirect
from category.models import Category
from .forms import categoryCreateForm, categoryEditForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def index_category(request):
    all_categories = Category.objects.all()
    context = {'categories': all_categories}
    return render(request, 'category/index.html', context)

@login_required
def create_category(request):
    if request.method == 'POST':
        form = categoryCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category has been created.')
            return redirect('index_category')
        else:
            messages.error(request, 'Category failed to create.')
    else:
        form = categoryCreateForm()
    
    context = {'form': form}
    return render(request, 'category/create.html', context)

@login_required
def update_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)

    if request.method == 'POST':
        form = categoryEditForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category has been updated.')
            return redirect('index_category')
        else:
            messages.error(request, 'Category failed to update.')
        print("Form errors:", form.errors)
    else:
        form = categoryEditForm(instance=category)

    context = {'form': form, 'category': category}
    return render(request, 'category/edit.html', context)

@login_required
def delete_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)

    if request.method == 'POST':
        category.delete()
        messages.success(request, 'Category has been deleted.')
        return redirect('index_category')
    else:
        messages.error(request, 'Category failed to delete.')

    context = {'category': category}
    return render(request, 'category/delete.html', context)
