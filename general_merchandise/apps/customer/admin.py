from django.contrib import admin
from django.apps import apps
from .models import Person

# Register your models here.

admin.site.register(Person)