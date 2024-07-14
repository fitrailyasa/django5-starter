from django import forms
from .models import Product

class productCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'desc', 'img', 'category_id']
        widgets = {
            'desc': forms.Textarea(attrs={'rows': 4}),
        }

class productEditForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'desc', 'img', 'category_id']
        widgets = {
            'desc': forms.Textarea(attrs={'rows': 4}),
        }
