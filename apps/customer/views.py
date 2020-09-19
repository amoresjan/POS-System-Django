from django.shortcuts import render,redirect
from django.views import View
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.

def customerDashboardViewSet(request):
    customers = Person.objects.all()
    return render(request, 'customer/dashboard.html', {'customers': customers})

    
#Customer CRUD

class customerRegistrationViewSet(View):
    customer_form = CustomerForm

    def get(self, request):
        context = {'form' : self.customer_form}
        return render(request, 'customer/registration_customer.html', context)

    def post(self, request):
        form = self.customer_form(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/')
        
        return HttpResponse(form.errors)
