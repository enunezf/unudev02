from django.contrib import admin

from miapp.models import Empleados

class EmpleadosAdmin(admin.ModelAdmin):
    pass


admin.site.register(Empleados, EmpleadosAdmin)