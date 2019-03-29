from django.shortcuts import render
from .models import Post

# Create your views here.
def blog(request):
    entries_list = Post.objects.all()
    return render(request, "blog/blog.html",{'entries':entries_list})
