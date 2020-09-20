from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.


def productDashboardViewSet(request):
    return render(request, 'product/dashboard.html')


class productRegistrationViewSet(View):
    product_form = ProductForm

    def get(self, request):
        context = {'form': self.product_form}
        return render(request, 'product/registration_product.html', context)

    def post(self, request):
        form = self.product_form(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('/')

        return HttpResponse(form.errors)
