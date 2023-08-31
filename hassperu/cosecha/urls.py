from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_productos, name='lista_productos'),
    #path('', views.lista_clientes, name='lista_clientes'),

]
