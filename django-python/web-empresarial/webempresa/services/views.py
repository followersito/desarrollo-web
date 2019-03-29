from django.shortcuts import render
from .models import Service

# Create your views here.
def services(request):
    service_list = Service.objects.all()
    return render(request, 'services/services.html',{'services':service_list})

