from django.contrib import admin
from .models import Empleados, Departamento, Beneficio, Salario
# Register your models here.

@admin.register (Empleados)
class EmpleadosAdmin(admin.ModelAdmin):
    list_display = ('cedula', 'nombre', 'apellido', 'direccion', 'email', 'telefono', 'cargo')
    search_fields = ('cedula', 'nombre', 'apellido')
    list_filter = ('cedula',)

@admin.register(Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion')
    search_fields = ('nombre',)
@admin.register(Beneficio)
class BeneficioAdmin(admin.ModelAdmin):
    list_display = ('empleado', 'tipo', 'descripcion', 'monto', 'fecha_asignacion')
    search_fields = ('empleado__nombre', 'tipo')
    list_filter = ('tipo',)
@admin.register(Salario)
class SalarioAdmin(admin.ModelAdmin):
    list_display = ('empleado', 'monto', 'fecha_pago')
    search_fields = ('empleado__nombre',)
    list_filter = ('fecha_pago',)
