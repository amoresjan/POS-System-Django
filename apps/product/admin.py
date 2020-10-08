from django.contrib import admin
from django.apps import apps
from .models import Product, Images

# Register your models here.

admin.site.register(Product)
admin.site.register(Images)
