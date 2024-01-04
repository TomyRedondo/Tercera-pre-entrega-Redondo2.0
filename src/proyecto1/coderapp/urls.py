from django.urls import path
from coderapp.views import profesores, estudiantes, cursos, entregables, index


urlpatterns = [
    path('profesores/', profesores, name='profesores'),
    path('estudiantes/', estudiantes, name='estudiantes'),
    path('cursos/', cursos, name='cursos'),
    path('entregable/', entregables, name='entregables'),
    path('', index),
]
