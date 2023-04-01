from django.shortcuts import render
from django.http import HttpResponse
from .models import Cancha,Persona
# Create your views here.

def getInfoCanchaById(request, id_cancha):
    #Obtener cancha por su id utilizando ORM
    cancha = Cancha.objects.get(id=id_cancha)
    result_layout = f"<h3>Cancha: {cancha.nombre}, Descripción: {cancha.descripcion}</h3>"

    return HttpResponse(result_layout)

def getPersonaById(request, id_persona):
    #Obtener persona por su id utilizando ORM
    persona = Persona.objects.get(id=id_persona)
    result_layout = f"<h3>Nombre: {persona.nombre}, Apellido: {persona.apellido}, Correo: {persona.correo}</h3>"

    return HttpResponse(result_layout)