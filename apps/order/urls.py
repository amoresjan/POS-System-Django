from django.urls import path
from apps.order import views

urlpatterns = [
    path('', views.orderDashboardView.as_view(), name='orderDashboard'),
]