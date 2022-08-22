from importlib.resources import path
from django.urls import path
from .views import *


urlpatterns = [
    path("curso/", curso),
    path("profesores/", profesores, name= "profesores"),
    path("entregables/", entregables, name= "entregables"),
    path("cursos/", cursos, name= "cursos"),
    path("estudiantes/", estudiantes, name= "estudiantes"),
    path("", inicio, name= "inicio"),






]
