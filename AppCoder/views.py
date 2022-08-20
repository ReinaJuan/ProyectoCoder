from django.http import HttpResponse
from django.shortcuts import render
from.models import Curso

# Create your views here.
def curso(request):

    
    curso=Curso(nombre="Curso de Python", comision=152785)
    curso.save()
    texto=f"Curso Creado: nombre: {curso.nombre} comision: {curso.comision}"
    return HttpResponse(texto)


def inicio(request):
    return render (request, "AppCoder/inicio.html")

def cursos(request):
    return render (request, "AppCoder/cursos.html")


def profesores(request):
    return render (request, "AppCoder/profesores.html")

def entregables(request):
    return render (request, "AppCoder/entregables.html")

def estudiantes(request):
    return render (request, "AppCoder/estudiantes.html")
