from rest_framework import serializers
from .models import Empleados, Departamento, Beneficio, Salario

class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleados
        fields = '__all__'

class DepartamentoSerializer(serializers.ModelSerializer):
    empleados = serializers.PrimaryKeyRelatedField(queryset=Empleados.objects.all(), many=True)  # 🔹 Relación corregida

    class Meta:
        model = Departamento
        fields = '__all__'

class BeneficioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beneficio
        fields = '__all__'

class SalarioSerializer(serializers.ModelSerializer):
    empleado = serializers.PrimaryKeyRelatedField(queryset=Empleados.objects.all())
    class Meta:
        model = Salario
        fields = '__all__'

