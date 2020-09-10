from django.urls import path
from . import views

urlpatterns = [
    path('', views.landingPageViewSet, name='landingPage'),
]