from django.urls import path
from . import views

urlpatterns = [
    path('getInfoCanchaById/<int:id_cancha>',views.getInfoCanchaById,name="getInfoCanchaById"),
    path('getPersonaById/<int:id_persona>',views.getPersonaById,name="getPersonaById"),
    path("", views.MainView.as_view()),
    path('canchas', views.getListadoCanchas, name="Listado de Canchas"),
    path("registro", views.registro_request, name='registro')
]

 #   path('getInfoCanchaById/<int:id_cancha>',views.getInfoCanchaById,name="getInfoCanchaById"),
  #  path('getPersonaById/<int:id_persona>',views.getPersonaById,name="getPersonaById")