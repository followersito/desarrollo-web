from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo")          # Campo de cadena de caracteres
    description = models.TextField(verbose_name="Descripción")            # Campo de texto
    image = models.ImageField(verbose_name="Imagen", upload_to="projects")         # Campo de imagen
    url_field = models.URLField(max_length=200, verbose_name="URL", blank=True, null=True)         # blank y null permiten el campo como Opcional
    created = models.DateTimeField(auto_now_add = True,verbose_name="Fecha de creación")         # Campo de fecha y hora (Se añade automaticamente al crear instancias)
    updated = models.DateTimeField(auto_now = True,verbose_name="Fecha de edición")             # Se actualiza cuando se modifica
   

    # Las clases y métodos declarados acá son para configuración extra a la clase en front end
    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        ordering = ["-created"]         # Se pone el guión para que se haga el orden a la inversa

    def __str__(self):
        return self.title
