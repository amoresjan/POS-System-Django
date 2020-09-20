from django.urls import path
from . import views

urlpatterns = [
    path('', views.productDashboardViewSet, name='productDashboard'),
    path('registration/', views.productRegistrationViewSet.as_view(), name='productRegistration')
]