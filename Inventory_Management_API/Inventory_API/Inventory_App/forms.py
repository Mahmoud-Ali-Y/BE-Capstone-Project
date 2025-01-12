from django import forms
from .models import Product
from django.contrib.auth.models import User

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'quantity', 'price', 'category']
        #fields = '__all__'
        labels = {
            'product_id': 'Product_ID',
            'name': 'Name',
            'description': 'Description',
            'quantity': 'Quantity',
            'price': 'Price',
            'category': 'Category',
            'date_added': 'Date Added',
            'last_updated': 'Last Updated',
        }
        widgets = {
            'product_id': forms.NumberInput(attrs={'placeholder':'e.g. 1', 'class':'form-control'}),
            'name': forms.TextInput(attrs={'placeholder':'e.g. screen protector', 'class':'form-control'}),
            'description': forms.TextInput(attrs={'placeholder':'e.g.  plastic material', 'class':'form-control'}),
            'quantity': forms.NumberInput(attrs={'placeholder':'e.g. 15', 'class':'form-control'}),
            'price': forms.NumberInput(attrs={'placeholder':'e.g. 99.99', 'class':'form-control'}),
            'category': forms.TextInput(attrs={'placeholder':'e.g. Accessories', 'class':'form-control'}),
        }

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password_confirm']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        # Check if th passwords match
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("passwords do not match!")
        return cleaned_data
    
class UpdateForm(forms.ModelForm):
    #password = forms.CharField(widget=forms.PasswordInput)
    #password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean(self):
        cleaned_data = super().clean()
        #password = cleaned_data.get('password')
        #password_confirm = cleaned_data.get('password_confirm')
        # Check if th passwords match
        #if password and password_confirm and password != password_confirm:
            #raise forms.ValidationError("passwords do not match!")
        return cleaned_data