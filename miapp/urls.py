from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='miapp_index'),
    path('empleados', views.empleados, name='empleados'),
]