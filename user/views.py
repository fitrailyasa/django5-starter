from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .forms import UserCreateForm, UserEditForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def index_user(request):
    all_users = User.objects.all()

    context = {'title': 'User', 'users': all_users}
    return render(request, 'user/index.html', context)

@login_required
def create_user(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, 'User has been created.')
            return redirect('index_user')
        else:
            messages.error(request, 'User failed to create.')
    else:
        form = UserCreateForm()

    context = {'form': form}
    return render(request, 'user/index.html', context)

@login_required
def update_user(request, user_id):
    user = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=user)
        if form.is_valid():
            user.set_password(form.cleaned_data['password'])
            form.save()
            messages.success(request, 'User has been updated.')
            return redirect('index_user')
        else:
            messages.error(request, 'User failed to update.')
    else:
        form = UserEditForm(instance=user)

    context = {'form': form, 'user': user}
    return render(request, 'user/index.html', context)

@login_required
def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        user.delete()
        messages.success(request, 'User has been deleted.')
        return redirect('index_user')
    else:
        messages.error(request, 'User failed to delete.')

    context = {'user': user}
    return render(request, 'user/index.html', context)