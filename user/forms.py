from django import forms
from django.contrib.auth.models import User

class UserCreateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not username:
            raise forms.ValidationError("Username cannot be empty!")
        if len(username) > 100:
            raise forms.ValidationError("Username cannot be longer than 100 characters!")
        return username
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError("Email cannot be empty!")
        if len(email) > 100:
            raise forms.ValidationError("Email cannot be longer than 100 characters!")
        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if not password:
            raise forms.ValidationError("Password cannot be empty!")
        if len(password) < 8:
            raise forms.ValidationError("Password must be at least 8 characters!")
        if len(password) > 255:
            raise forms.ValidationError("Password cannot be longer than 255 characters!")
        return password

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not username:
            raise forms.ValidationError("Username cannot be empty!")
        if len(username) > 100:
            raise forms.ValidationError("Username cannot be longer than 100 characters!")
        return username
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError("Email cannot be empty!")
        if len(email) > 100:
            raise forms.ValidationError("Email cannot be longer than 100 characters!")
        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise forms.ValidationError("Password must be at least 8 characters!")
        if len(password) > 255:
            raise forms.ValidationError("Password cannot be longer than 255 characters!")
        return password