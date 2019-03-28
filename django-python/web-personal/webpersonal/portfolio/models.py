from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)          # Campo de cadena de caracteres
    description = models.TextField()            # Campo de texto
    image = models.ImageField()         # Campo de imagen
    created = models.DateTimeField(auto_now_add = True)         # Campo de fecha y hora (Se añade automaticamente al crear instancias)
    updated = models.DateTimeField(auto_now = True)             # Se actualiza cuando se modifica

