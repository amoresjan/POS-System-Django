from django.shortcuts import render

# Create your views here.

def productDashboardViewSet(request):
    return render(request, 'product/dashboard.html')

def productRegistrationViewSet(request):
    return render(request, 'product/registration_product.html')