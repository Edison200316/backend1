from django.db import models
from .choices import CARGO
from django.core.validators import MinLengthValidator, MinValueValidator, MaxLengthValidator, MaxValueValidator
from .validadores import validacion_numeros

class Empleados(models.Model):
    cedula = models.CharField(max_length=10, primary_key=True,validators=[MinLengthValidator(10), MaxLengthValidator(10), validacion_numeros])
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

class Departamento(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    empleados = models.ManyToManyField(Empleados, related_name='departamentos') 

    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'
        db_table = 'Departamentos'


    def __str__(self):
        return self.nombre

class Beneficio(models.Model):
    TIPO_BENEFICIO = [('seguro', 'Seguro Médico'),('bono', 'Bono de Rendimiento'),
                      ('vacaciones', 'Días de Vacaciones'),('otro', 'Otro'),]
    empleado = models.ForeignKey(Empleados, on_delete=models.CASCADE, related_name='beneficios')
    tipo = models.CharField(max_length=50, choices=TIPO_BENEFICIO)
    descripcion = models.TextField()
    monto = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    fecha_asignacion = models.DateField()

    class Meta:
        verbose_name = 'Beneficio'
        verbose_name_plural = 'Beneficios'
        db_table = 'Beneficios'

    def __str__(self):
        return f"Beneficio de {self.empleado.nombre} - {self.tipo}"

class Salario(models.Model):
    empleado = models.ForeignKey(Empleados, on_delete=models.CASCADE, related_name='salarios')
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_pago = models.DateField()

    class Meta:
        verbose_name = 'Salario'
        verbose_name_plural = 'Salarios'
        db_table = 'Salarios'

    def __str__(self):
        return f"Salario de {self.empleado.nombre} - {self.monto}"