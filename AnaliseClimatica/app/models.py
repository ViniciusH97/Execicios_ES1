from django.db import models

class Pais(models.Model):
    nome = models.CharField(max_length=40)
    
    def __str__(self):
        return self.nome

class Continentes(models.Model):
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
    temperatura = models.DecimalField(max_digits=2, decimal_places=2)
    clima = models.ForeignKey(Clima, on_delete=models.CASCADE)
    
    
    
    def __str__(self):
        return self.nome
    
class DadosClimatico(models.Model):
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    clima = models.CharField(max_length=30)
    graus = models.DecimalField(max_digits=2, decimal_places=2)
    
    def __str__(self):
        return f' {self.pais} {self.clima} {self.graus}'
    