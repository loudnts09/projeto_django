from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar_pizza/', views.cadastrar_pizza, name='cadastrar_pizza'),
]
