from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
def validacion_numeros(value):
    if not value.isdigit():
        raise ValidationError("El valor debe contener solo números")