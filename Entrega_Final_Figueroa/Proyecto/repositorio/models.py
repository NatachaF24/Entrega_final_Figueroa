from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Complejo(models.Model):
    complejo = models.CharField(max_length=50)
    direccion = models.CharField(max_length=80)
    telefono = models.IntegerField()
    
    def __str__(self):
        return f"{self.complejo}"

class Profesor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    complejo = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = "Profesor"
        verbose_name_plural = "Profesores"
    
    def __str__(self):
        return f"{self.nombre}, {self.apellido}, {self.complejo}"

class Profesional(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    profesion = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = "Profesional"
        verbose_name_plural = "Profesionales"
    
    def __str__(self):
        return f"{self.nombre}, {self.apellido}, {self.profesion}"
    
class Responsable(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    posicion = models.CharField(max_length=60)

    def __str__(self):
        return f"{self.nombre}, {self.apellido}, {self.posicion}" 

class Avatar(models.Model):   
    imagen = models.ImageField(upload_to="avatares") 
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.imagen}" 