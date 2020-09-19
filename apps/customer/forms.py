from django.forms import ModelForm
from django_countries.widgets import CountrySelectWidget
from .models import *

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ('first_name',)