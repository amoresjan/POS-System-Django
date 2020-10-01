from django.forms import ModelForm,ModelChoiceField
from django_countries.widgets import CountrySelectWidget
from .models import *
from apps.customer import choices

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
    widgets = {
        'country': CountrySelectWidget()
    }