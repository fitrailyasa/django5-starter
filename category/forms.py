from django import forms
from category.models import Category

class categoryCreateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'desc', 'img']
        widgets = {
            'desc': forms.Textarea(attrs={'rows': 4}),
        }

class categoryEditForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'desc', 'img']
        widgets = {
            'desc': forms.Textarea(attrs={'rows': 4}),
        }