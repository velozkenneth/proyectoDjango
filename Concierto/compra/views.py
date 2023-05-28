from typing import Any, Dict
from django.contrib.auth.mixins import LoginRequiredMixin #Para invocar la vista solo si esta autenticado
from .forms import RegistroForm, LoginForm, CompraForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, DetailView
from .models import Concierto, Persona, Compra, Ubicacion, Ticket, CompraStatus
from django.contrib import messages
from django.utils.timezone import now
# Create your views here.

class MainView(TemplateView): #Pantalla principal
    template_name = "compra/main.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["conciertos"] = Concierto.objects.all()
        return context

class ConciertoView(DetailView): #DetailView permite buscar por detalle cada elemento del modelo ej. /concierto/1
    model = Concierto
    template_name = "compra/concierto_detalle.html"
    context_object_name = "concierto" #palabra clave en el HTML

class TicketsView(TemplateView, LoginRequiredMixin):
    template_name = "compra/tickets.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        user = self.request.user
        persona = Persona.objects.get(user=user) #Obtiene la persona asociada al user
        tickets = Ticket.objects.filter(compra__persona=persona) #Obtiene los tickets asociados a la persona, mediante filtro de 'compra' por el parametro persona
        compras = Compra.objects.filter(persona=persona)
        context['tickets'] = tickets
        print(tickets)
        return context

class CompraStatusView(TemplateView, LoginRequiredMixin):
    template_name = "compra/compras_status.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        user = self.request.user
        persona = Persona.objects.get(user=user) #Obtiene la persona asociada al user
        compras = CompraStatus.objects.filter(compra__persona=persona) #Compras asociadas y su status
        context['compras'] = compras
        return context

def registroView(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            messages.success(request,"Ha completado correctamente el registro!")
            return redirect("/")
    else:
        form = RegistroForm()
        messages.error(request,"Informacion incorrecta, vuelva a intentarlo")
    return render(request, 'compra/registro.html', {'form': form})

def loginView(request):
    if request.method == 'POST':
        form = LoginForm(request.POST, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Ha iniciado sesion como: {username}")
                return redirect('Home')
            messages.error(request, "Credenciales incorrectas")
        messages.error(request, "Datos proporcionados incorrectos")
    else:
        form = LoginForm()
    return render(request, 'compra/login.html', {'form': form})

def logoutView(request):
    logout(request)
    messages.info(request, "Has cerrado sesión")
    return redirect("Login")

def compraView(request, concierto_id):
    if request.method == "POST":
        compra_form = CompraForm(data=request.POST)
        if compra_form.is_valid():
            user_id = request.user.id
            c_num_tickets = int(compra_form.data["num_tickets"])
            c_persona = Persona.objects.get(user__id=user_id)
            c_concierto = Concierto.objects.get(id=concierto_id)
            c_ubicacion = Ubicacion.objects.get(id=compra_form.data["ubicacion"])

            capacidad = int(c_concierto.capacidad) #capacidad total
            #print(capacidad)
            tickets = Ticket.objects.all() #tickets vendidos
            
            # Validar disponibilidad
            if c_num_tickets<=capacidad and c_num_tickets<=(capacidad - len(tickets)):

                # Guardo en la tabla de Compra
                compra = Compra(persona=c_persona,concierto = c_concierto, num_tickets = c_num_tickets,ubicacion = c_ubicacion)
                compra.save()
                
                #Ahora guardo el status de CompraStatus
                costo_total = c_concierto.precio_ticket * c_num_tickets
                compra_status = CompraStatus(compra=compra, status = True, total = costo_total)
                compra_status.save()

                #Almacenar los codigos de los tickets
                
                last_codigo = 0 if len(tickets)==0 else int(tickets.last().codigo) #obtengo el ultimo codigo

                for i in range(c_num_tickets): #Registra el codigo
                    last_codigo+=1
                    ticket = Ticket(codigo=last_codigo,compra=compra)
                    ticket.save()
                #print(c_concierto.capacidad)
                c_concierto.capacidad -= (c_num_tickets)
                c_concierto.save()
                messages.success(request, f"Felicidades! Has comprado {c_num_tickets} tickets para ver a {c_concierto.artista} en su gira {c_concierto.titulo}")
                return redirect("Home")
            else:
                messages.error(request, 'El número de tickets solicitados supera a la capacidad máxima')
                
    else:
        c_concierto = Concierto.objects.get(id=concierto_id)
        compra_form = CompraForm(initial={"concierto" : concierto_id})
    return render(request, "compra/compra.html", {"compra_form" : compra_form, "concierto" : c_concierto})

def cancelarView(request,compra_status_id):
    compra_status = CompraStatus.objects.get(id=compra_status_id)
    fecha_concierto = compra_status.compra.concierto.fecha
    diferencia_dias = (fecha_concierto - now()).days
    print("Dias para el concierto: \n",diferencia_dias)
    if diferencia_dias>=2:
        compra_status.status = False
        compra = compra_status.compra
        compra_status.save()
        tickets = Ticket.objects.filter(compra=compra)
        
        #Actualiza la capacidad
        concierto = Concierto.objects.get(id=compra.concierto.id)
        concierto.capacidad += len(tickets)
        concierto.save()

        #Borra los tickets
        tickets.delete()
        messages.success(request, "Has cancelado correctamente")
    else:
        messages.info(request,"Lo sentimos, solo puedes cancelar hasta 2 dias antes del concierto.")
    return redirect('Tickets')
    