from django.urls import path
from .views import (
    MainView, 
    ConciertoView,
    TicketsView,
    CompraStatusView, 
    registroView,
    loginView, 
    logoutView, 
    compraView,
    cancelarView
    )

urlpatterns = [
    path('', MainView.as_view(),name="Home"),
    path('concierto/<int:pk>', ConciertoView.as_view(), name="concierto-detail"),
    path('login/',loginView, name="Login"),
    path('logout/',logoutView, name="Logout"),
    path('registro/',registroView, name="Registro"),
    path('compra/<int:concierto_id>',compraView, name="Compra"),
    path('tickets/', TicketsView.as_view(), name="Tickets"),
    path('compras/',CompraStatusView.as_view(),name="Compras"),
    path('cancelar/<int:compra_status_id>', cancelarView, name='Cancelar')
]