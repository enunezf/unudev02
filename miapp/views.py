from django.shortcuts import render
from django.conf import settings

from .models import Empleados

def index(request):
    nombreEmpresa = settings.NOMBRE_EMPRESA
    return render(request, 'miapp/index.html', {'nombreEmpresa':nombreEmpresa})

def empleados(request):
    empleados = Empleados.objects.all()
    return render(request, 'miapp/empleados.html', {'empleados':empleados})