from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def customerDashboardViewSet(request):
    customers = Person.objects.all()
    return render(request, 'customer/dashboard.html', {'customers': customers})

def customerRegistrationViewSet(request):
    return render(request, 'customer/registration_customer.html')