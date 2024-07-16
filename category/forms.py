from django import forms
from category.models import Category

class categoryCreateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'desc', 'img']
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

class categoryEditForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'desc', 'img']
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
