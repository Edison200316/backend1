from django.shortcuts import render
from rest_framework import viewsets
from .models import Empleados, Departamento, Beneficio, Salario
from .serializers import EmpleadoSerializer, DepartamentoSerializer, BeneficioSerializer, SalarioSerializer
from rest_framework.permissions import AllowAny

# Vista para el modelo Empleados
class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset = Empleados.objects.all()
    serializer_class = EmpleadoSerializer
    permission_classes = [AllowAny]

# Vista para el modelo Departamento
class DepartamentoViewSet(viewsets.ModelViewSet):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer
    permission_classes = [AllowAny]

# Vista para el modelo Beneficio
class BeneficioViewSet(viewsets.ModelViewSet):
    queryset = Beneficio.objects.all()
    serializer_class = BeneficioSerializer
    permission_classes = [AllowAny]

# Vista para el modelo Salario
class SalarioViewSet(viewsets.ModelViewSet):
    queryset = Salario.objects.all()
    serializer_class = SalarioSerializer
    permission_classes = [AllowAny]
