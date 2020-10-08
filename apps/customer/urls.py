from django.urls import path
from . import views

urlpatterns = [
    path('', views.customerDashboardView.as_view(), name='customerDashboard'),
    path('registration/', views.customerRegistrationView.as_view() , name='customerRegistration')
]