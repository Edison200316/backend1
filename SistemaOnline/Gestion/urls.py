from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmpleadoViewSet, DepartamentoViewSet, BeneficioViewSet, SalarioViewSet


# Crea un router y registra las vistas
router = DefaultRouter()
router.register(r'empleados', EmpleadoViewSet)
router.register(r'departamentos', DepartamentoViewSet)
router.register(r'beneficios', BeneficioViewSet)
router.register(r'salarios', SalarioViewSet)

# Define las URLs de la API
urlpatterns = [
    path('', include(router.urls)),
]
