from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar_pedido/', views.cadastrar_pedido, name='cadastrar_pedido'),
]
