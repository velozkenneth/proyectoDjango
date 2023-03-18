from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def hello(request):
    return HttpResponse("Hello contéstame el Teléfono!")

def pagina(request):
    return HttpResponse(
        """
        <h1> Página de mi web </h1>
        """
    )
