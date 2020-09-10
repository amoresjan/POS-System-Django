from django.shortcuts import render

# Create your views here.

def landingPageViewSet(request):
    return render(request, 'landing_page/index.html')