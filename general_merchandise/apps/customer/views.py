from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def customerDashboardViewSet(request):
    return render(request, 'customer/dashboard.html')

def customerRegistrationViewSet(request):
    return render(request, 'customer/registration_customer.html')