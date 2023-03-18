from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hola', views.hello, name="Hola"),
    path('pagina-pruebas', views.pagina, name="pagina")
]
