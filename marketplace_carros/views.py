from django.shortcuts import render
from marketplace_carros import models

def lista_de_carros(request):
  carro = Carros.objects.all()
  return render (request, 'marketplace/lista-de-carros.html', {'carro': carro})
