from django.contrib import admin
from .models import Service

# Clases que son solo de lectura en el panel de administrador (Configuracion de la clase en panel)
class ServicesAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

# Registro de modelos en el panel de administrador
admin.site.register(Service, ServicesAdmin)