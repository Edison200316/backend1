from django.db import models
from .choices import CARGO
from django.core.validators import MinLengthValidator,MinValueValidator,MaxLengthValidator,MaxValueValidator
from .validadores import validacion_numeros

# Create your models here.
class Empleados(models.Model):
    cedula = models.CharField(max_length=10, primary_key=True, validators=[MinLengthValidator(10), validacion_numeros])
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50, verbose_name="Apellido dd")
    direccion = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)
    cargo = models.CharField(max_length=50, choices=CARGO)
    
    class Meta:
        verbose_name = 'Empleado xx'
        verbose_name_plural = 'Empleados yy'
        db_table = 'Empleados'
        
    def __str__(self):
        return self.nombre + ' ' + self.apellido