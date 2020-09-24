from django.shortcuts import render, redirect
from django.forms import modelformset_factory
from django.views import View
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.


def productDashboardViewSet(request):
    products = Product.objects.all()
    return render(request, 'product/dashboard.html', {'products': products})


class productRegistrationViewSet(View):
    product_form = ProductForm
    ImageFormSet = modelformset_factory(Images, fields=('image',), extra=4)

    def get(self, request):
        ImageFormSet = modelformset_factory(Images, fields=('image',), extra=3)
        formset = ImageFormSet(queryset=Images.objects.none())
        context = {'form': self.product_form, 'formset': formset}
        return render(request, 'product/registration_product.html', context)

    def post(self, request):
        ImageFormSet = modelformset_factory(Images, fields=('image',), extra=3)
        form = self.product_form(request.POST, request.FILES)
        formset = ImageFormSet(request.POST or None, request.FILES or None)
        if form.is_valid() and formset.is_valid():
            product = form.save(commit=False)
            product.save()

            for f in formset:
                try:
                    photo = Images(product=product,
                                   image=f.cleaned_data['image'])
                    photo.save()
                except Exception as e:
                    break
            return redirect('/product')

        return HttpResponse(form.errors)
