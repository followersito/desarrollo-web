from django.shortcuts import render, get_object_or_404          # Funcion para obtener pagina 404 si no se encuentra
from .models import Post, Category

# Create your views here.
def blog(request):
    entries_list = Post.objects.all()
    return render(request, "blog/blog.html",{'entries':entries_list})

def category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    
    return render(request, "blog/category.html", {'category':category})

