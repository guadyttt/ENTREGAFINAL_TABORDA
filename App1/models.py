from django.db import models
from django.contrib.auth.models import User

class Curso(models.Model):
    nombre = models.CharField(max_length=50)
    comision = models.IntegerField()
    def __str__(self):
        return f"{self.nombre}, {self.comision}"

class Alumno(models.Model):
    nombre = models.CharField(max_length=50)
    dni = models.IntegerField()
    def __str__(self):
        return f"{self.nombre}, {self.dni}"

class Profesor(models.Model):
    nombre = models.CharField(max_length=50)
    dni = models.IntegerField()
    def __str__(self):
        return f"{self.nombre}, {self.dni}"
    
class Avatar(models.Model):
    user = models.ForeignKey( User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null= True, blank=True)
    
    def __str__(self):

        return f"User: {self.user}  -  Imagen: {self.imagen}"
    
    def clean(self):
        from django.core.exceptions import ValidationError
        from PIL import Image
        
        super().clean()
        if self.imagen:
            try:
                img = Image.open(self.imagen)
                img.verify()
            except Exception:
                raise ValidationError("El archivo seleccionado no es una imagen válida.")

    def image_url(self):
        if self.imagen:
            return self.imagen.url
        else:
            return "/path/to/default/avatar.jpg"
    
