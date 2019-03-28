from django.shortcuts import render, HttpResponse

html_base = """
<h1>Mi web personal</h1>
<ul>
    <li><a href="/">Portada</a></li>
    <li><a href="/about-me/">Acerca de</a></li>
    <li><a href="/portfolio/">Portafolio</a></li>
    <li><a href="/contact/">Contacto</a></li>
</ul>
"""
# Create your views here.
def home(request):
   # html_response = "<h1> Mi web personal</h1>"
   # for i in range(10):
      #  html_response += "<h2>Portada</h2>"
    return HttpResponse(html_base+"""
    <h2>Esto es la portada</h2>
    """)

def about(request):
    return HttpResponse(html_base+"<h1>Acerca de</h1><p>Me llamo Ivan<p>")

def portfolio(request):
    return HttpResponse(html_base + "<h1>Portafolio</h1><p>Esta es la pagina de portafolio<p>")

def contact(request):
    return HttpResponse(html_base+"<h1>Contacto</h1><p>Este es el apartado de contacto<p>")
