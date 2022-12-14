from django.db import models

# Create your models here.

class Curso (models.Model):
    nombre_curso = models.CharField(max_length=50)
    numero_comision = models.IntegerField()

    def __str__ (self):
        return f'{self.nombre} - {str(self.comision)}'

class Estudiante (models.Model):
    nombre = models.CharField (max_length=60)
    apellido= models.CharField (max_length=60)
    email = models.EmailField()

    def __str__ (self):
        return f'{self.nombre} - {self.apellido}'

class Profesor (models.Model):
    nombre = models.CharField (max_length=60)
    apellido= models.CharField (max_length=60)
    email = models.EmailField()
    profesion = models.CharField(max_length=50)

    def __str__ (self):
        return f'{self.nombre} - {self.apellido}'

class Entregable (models.Model):
    nombre = models.CharField (max_length=60)
    fecha_entrega = models.DateField()
    entregado = models.BooleanField()

    def __str__ (self):
        return f'{self.nombre} - {self.entregado}'


