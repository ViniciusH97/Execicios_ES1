from django.db import models


class Usuario(models.Model):
    nome = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    senha = models.CharField(max_length=40)

class Pais(models.Model):
    nome = models.CharField(max_length=40)
    
    def __str__(self):
        return self.nome

class Continente(models.Model):
    nome = models.CharField(max_length=40)
    paises = models.ForeignKey(Pais,on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.nome} {self.paises}'
    
class Clima(models.Model):
    nome = models.CharField(max_length=40)
    
    def __str__(self):
        return self.nome
    
class Estado(models.Model):
    nome = models.CharField(max_length=30)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    clima = models.ForeignKey(Clima, on_delete=models.CASCADE)
    temperatura = models.DecimalField(max_digits=4, decimal_places=2)
    
    def __str__(self):
        return self.nome
