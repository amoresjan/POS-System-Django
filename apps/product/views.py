from django.shortcuts import render, redirect
from django.forms import modelformset_factory
from django.views import View
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.


class productDashboardViewSet(View):
    def get(self, request):
        products = Product.objects.all()
        context = {
             'products': products,
             'color_choices' : choices.Color,
        }
        return render(request, 'product/dashboard.html', context)

    def post(self, request):
        if request.method == 'POST':
            if 'btnUpdate' in request.POST:
                sku = request.POST.get("sku")
                category = request.POST.get("product_category")
                brand = request.POST.get("product_brand")
                col = request.POST.get("color")
                name = request.POST.get("product_name")
                price = request.POST.get("product_price")
                num = request.POST.get("num_items")
                update_product = Product.objects.filter(sku = sku).update(product_category = category, product_brand = brand, color = col, product_name = name, product_price = price, num_items = num)
                print(update_product)
                print('product updated')

            elif 'btnDelete' in request.POST:
                sku = request.POST.get("sku")
                prod = Product.objects.filter(sku = sku).delete()

            
        return redirect('/product')



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


class productOrderViewSet(View):
    def get(self, request):
        products = Product.objects.all()
        context = {
            'products': products,
        }
        return render(request, 'product/order.html', context)

