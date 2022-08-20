from importlib.resources import path
from django.urls import path
from .views import *


urlpatterns = [
    path("curso/", curso),
    path("profesores/", profesores),
    path("entregables/", entregables),
    path("cursos/", cursos),
    path("estudiantes/", estudiantes),
    path("", inicio),






]
