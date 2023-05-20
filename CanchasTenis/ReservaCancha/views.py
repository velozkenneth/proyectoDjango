from django.shortcuts import render,redirect, HttpResponse
from .models import Cancha, Persona,Horario
from django.views.generic import TemplateView
from django.contrib.auth import login
from django.contrib import messages
from .forms import RegistroForm

# Create your views here.

def getInfoCanchaById(request, id_cancha):
    #Obtener cancha por su id utilizando ORM
    cancha = Cancha.objects.get(id=id_cancha)
    horarios = Horario.objects.filter(cancha__id=cancha.id) #doble subguion para indicar que pertenece a cancha el id
    #result_layout = f"<h3>Cancha: {cancha.nombre}, Descripción: {cancha.descripcion}</h3>"
    #return render(request,"cancha.html", {'nombre': cancha.nombre, 'descripcion' : cancha.descripcion})
    return render(request,"info_cancha.html", {'nombre': cancha.nombre, 'descripcion' : cancha.descripcion, 'horarios' : horarios})

def getPersonaById(request, id_persona):
    #Obtener persona por su id utilizando ORM
    persona = Persona.objects.get(id=id_persona)
    result_layout = f"<h3>Nombre: {persona.nombre}, Apellido: {persona.apellido}, Correo: {persona.correo}</h3>"

    return HttpResponse(result_layout)

class MainView(TemplateView):
    template_name = "main.html"

def getListadoCanchas(request):
    canchas = Cancha.objects.all()
    nombre_canchas = []

    for cancha in canchas:
        nombre_canchas.append((cancha.id, cancha.nombre))
    
    return render(request,"canchas.html", {'listado': nombre_canchas})

def registro_request(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Se ha registrado exitosamente')
            return redirect("landing")
        messages.error(request, 'Información no válida')
    form = RegistroForm()
    return render(request=request,template_name='registro.html',context={'registro_form': form})