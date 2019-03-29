from django.shortcuts import render
from .models import Project

# Create your views here.

def portfolio(request):
    project_list = Project.objects.all()
    return render(request, 'portfolio/portfolio.html', {'projects':project_list})

