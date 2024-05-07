from django.db import models

class Carros(models.Model):
  
  marca = models.CharField(max_length=50)
  modelo = models.CharField(max_length=100)
  ano = models.PositiveIntegerField()
  cor = models.CharField(max_length=20, blank=True)
  preco = models.DecimalField(max_digits=7, decimal_places=2)
  descricao = models.TextField()
  
  
  def __str__(self):
    return self.marca
  

 

