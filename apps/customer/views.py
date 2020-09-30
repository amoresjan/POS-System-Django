from django.shortcuts import render,redirect
from django.views import View
from django.http import HttpResponse
from apps.customer.models import Customer
from apps.customer.forms import CustomerForm
from apps.customer import choices

# Create your views here.

class customerDashboardView(View):
    customer_form = CustomerForm

    def get(self, request):
        customers = Customer.objects.all() 
        context = {
            'customers': customers,
            'status_choices' : choices.Status,
            'gender_choices' : choices.Gender
        }
        return render(request, 'customer/dashboard.html', context)

    def post(self, request):
        customer = Customer.objects.get(id = request.POST.get('id'))

        if 'btnUpdate' in request.POST:
            form = self.customer_form(request.POST, request.FILES, instance=customer)

            if form.is_valid():
                form.save()
                return redirect('customerDashboard')

            return HttpResponse(form.errors)

        elif 'btnDelete' in request.POST:
            customer.delete()
            return redirect('customerDashboard')


class customerRegistrationView(View):
    customer_form = CustomerForm

    def get(self, request):
        context = {'form' : self.customer_form}
        return render(request, 'customer/registration_customer.html', context)

    def post(self, request):
        form = self.customer_form(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('customerDashboard')
        
        return HttpResponse(form.errors)

