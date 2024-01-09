from django.http import HttpResponse
from django.shortcuts import render
from coderapp.models import Profesor


def leer_profesor(request):
    print("Vista Profesor")
    profe = Profesor(nombre="Alicia", apellido="Japo", email="ali.japo@test.com")
    profe.save()
    return HttpResponse("El profesor se creo exitosamente")


def leer_alumnos(request):
    contexto = {
        "nombre": "Milu",
        "apellido": "Ibañez",
        "edad": 29,
        "cursos": ["Alemán", "Japonés", "Doctorado Bioq."]
    }
    return render(request, 'plantilla.html', contexto)

def index(request):
    return render(request, 'index.html')

def profesores(request):
    return render(request, 'profesores.html')

def estudiantes(request):
    return render(request, 'estudiantes.html')

def cursos(request):
    return render(request, 'cursos.html')

def entregables(request):
    return render(request, 'entregables.html')