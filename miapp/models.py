from django.db import models


class Empleados(models.Model):

    nombre = models.CharField(max_length=200)
    cargo = models.CharField(max_length=50)
    edad = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"

    def __str__(self):
        return self.nombre


class Productos(models.Model):

    nombre = models.CharField(max_length=200)
    valor = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return self.nombre
