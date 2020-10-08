from django.urls import path
from . import views


urlpatterns = [
    path('', views.productDashboardViewSet.as_view(), name='productDashboard'),
    path('registration/', views.productRegistrationViewSet.as_view(),
         name='productRegistration'),
    path('order/', views.productOrderViewSet.as_view(), name='productOrder'),
    


]
