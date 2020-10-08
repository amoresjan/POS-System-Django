from django import forms
from django.forms import ModelForm
from .models import Product, Images


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class ImageForm(ProductForm):
    image = forms.ImageField(label='Image')

    class Meta:
        fields = ('image', )
