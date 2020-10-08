from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from apps.product.models import Product
from apps.order.models import Order
from apps.customer.models import Customer
from apps.order.forms import OrderForm

# Create your views here.

class orderDashboardView(View):
    order_form = OrderForm
    
    def get(self, request):
        customers = Customer.objects.all()
        products = Product.objects.all()
        context = {
            'customers' : customers,
            'products' : products,
        }
        return render(request, 'order/dashboard.html', context)

    def post(self, request):
        form = self.order_form(request.POST)

        if form.is_valid():
            form.save()
            return redirect('orderDashboard')

        return HttpResponse(form.errors)
