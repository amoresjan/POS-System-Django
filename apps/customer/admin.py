from django.contrib import admin
from django.apps import apps
from .models import *

# Register your models here.

admin.site.register(Person)
admin.site.register(Customer)