from django.contrib import admin
from .models import Empleados
# Register your models here.

@admin.register (Empleados)
class EmpleadosAdmin(admin.ModelAdmin):
    list_display = ('cedula', 'nombre', 'apellido', 'direccion', 'email', 'telefono', 'cargo')
    search_fields = ('cedula', 'nombre', 'apellido')
    list_filter = ('cedula', 'apellido')

