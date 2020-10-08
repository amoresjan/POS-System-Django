from django.forms import ModelForm, ModelChoiceField
from apps.order.models import Order

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'