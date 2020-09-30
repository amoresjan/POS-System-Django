from django.urls import path
from . import views

urlpatterns = [
    path('', views.customerView.as_view(), name='customerDashboard'),
    path('registration/', views.customerView.as_view(), name='customerRegistration')
]