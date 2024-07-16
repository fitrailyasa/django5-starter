from django import forms
from .models import Product

class productCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'desc', 'img', 'category_id']
        widgets = {
            'desc': forms.Textarea(attrs={'rows': 4}),
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            raise forms.ValidationError("Name cannot be empty!")
        if len(name) > 100:
            raise forms.ValidationError("Name cannot be longer than 100 characters!")
        return name
    
    def clean_price(self):
        price = self.cleaned_data.get('price')
        if not price:
            raise forms.ValidationError("Price cannot be empty!")
        if price < 0:
            raise forms.ValidationError("Price cannot be negative!")
        return price
    
    def clean_desc(self):
        desc = self.cleaned_data.get('desc')
        if len(desc) > 255:
            raise forms.ValidationError("Description cannot be longer than 255 characters!")
        return desc
    
    def clean_img(self):
        img = self.cleaned_data.get('img')
        if not img.name.endswith('.jpg') and not img.name.endswith('.png') and not img.name.endswith('.jpeg'):
            raise forms.ValidationError("Image type must be jpg, png, jpeg")
        if img.size > 2 * 1024 * 1024:
            raise forms.ValidationError("Image size must be less than 2 MB")
        return img
    
    def clean_category_id(self):
        category_id = self.cleaned_data.get('category_id')
        if not category_id:
            raise forms.ValidationError("Category cannot be empty!")
        return category_id

class productEditForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'desc', 'img', 'category_id']
        widgets = {
            'desc': forms.Textarea(attrs={'rows': 4}),
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            raise forms.ValidationError("Name cannot be empty!")
        if len(name) > 100:
            raise forms.ValidationError("Name tidak boleh lebih dari 100 karakter")
        return name
    
    def clean_price(self):
        price = self.cleaned_data.get('price')
        if not price:
            raise forms.ValidationError("Price cannot be empty!")
        if price < 0:
            raise forms.ValidationError("Price cannot be negative!")
        return price
    
    def clean_desc(self):
        desc = self.cleaned_data.get('desc')
        if len(desc) > 255:
            raise forms.ValidationError("Description cannot be longer than 255 characters!")
        return desc
    
    def clean_img(self):
        img = self.cleaned_data.get('img')
        if not img.name.endswith('.jpg') and not img.name.endswith('.png') and not img.name.endswith('.jpeg'):
            raise forms.ValidationError("Image type must be jpg, png, jpeg")
        if img.size > 2 * 1024 * 1024:
            raise forms.ValidationError("Image size must be less than 2 MB")
        return img
    
    def clean_category_id(self):
        category_id = self.cleaned_data.get('category_id')
        if not category_id:
            raise forms.ValidationError("Category cannot be empty!")
        return category_id
