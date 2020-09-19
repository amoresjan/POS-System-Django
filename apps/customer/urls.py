from django.urls import path
from . import views

urlpatterns = [
    path('', views.customerDashboardViewSet, name='customerDashboard'),
    path('registration/', views.customerRegistrationViewSet.as_view(), name='customerRegistration')
]