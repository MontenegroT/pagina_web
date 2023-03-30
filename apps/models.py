from django.db import models
# Create your models here.

class usuario(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    usename=models.CharField(max_length=30)
    email=models.EmailField()
    contrasena=models.CharField(max_length=30)
    def __str__(self):
        return self.nombre

class libros(models.Model):
    titulo=models.CharField(max_length=30)
    autor=models.CharField(max_length=30)
    genero=models.CharField(max_length=30)
    paginas=models.IntegerField()
    def __str__(self):
        return self.titulo


