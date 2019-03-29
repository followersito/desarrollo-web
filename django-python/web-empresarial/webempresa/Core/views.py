from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, "Core/index.html")

def about(request):
    return render(request, "Core/about.html")

def services(request):
    return render(request, "Core/services.html")

def store(request):
    return render(request, "Core/store.html")

def contact(request):
    return render(request, "Core/contact.html")

def blog(request):
    return render(request, "Core/blog.html")

def sample(request):
    return render(request, "Core/sample.html")