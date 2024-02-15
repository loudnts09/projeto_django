from django.urls import path
from . import views

urlpatterns = [
    path('cliente/int:cliente_id/', views.cadastrar_cliente, name='cadastrar_cliente'),
]
