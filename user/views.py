from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .forms import UserCreateForm, UserEditForm
from django.contrib import messages

def dashboard(request):
    return render(request, 'dashboard.html')

def index_user(request):
    all_users = User.objects.all()

    context = {'users': all_users}
    return render(request, 'user/index.html', context)

def create_user(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Meng-hash password
            user.save()
            messages.success(request, 'User berhasil dibuat.')
            return redirect('index_user')
        else:
            messages.error(request, 'Terjadi kesalahan saat membuat user.')
    else:
        form = UserCreateForm()

    context = {'form': form}
    return render(request, 'user/index.html', context)

def update_user(request, user_id):
    user = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=user)
        if form.is_valid():
            user.set_password(form.cleaned_data['password'])  # Meng-hash password baru jika ada perubahan
            form.save()
            messages.success(request, 'User berhasil diperbarui.')
            return redirect('index_user')
        else:
            messages.error(request, 'Terjadi kesalahan saat memperbarui user.')
    else:
        form = UserEditForm(instance=user)

    context = {'form': form, 'user': user}
    return render(request, 'user/index.html', context)

def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        user.delete()
        messages.success(request, 'User berhasil dihapus.')
        return redirect('index_user')
    else:
        messages.error(request, 'Terjadi kesalahan saat menghapus user.')

    context = {'user': user}
    return render(request, 'user/index.html', context)