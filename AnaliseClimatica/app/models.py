from django.db import models

class Pais(models.Model):
    nome = models.CharField(max_length=40)
    area = models.CharField(max_length=30)
    clima = models.CharField(max_length=30)
    bioma = models.CharField(max_length=30)
    
    def __str__(self):
        return f'{self.nome} {self.area}'

class Continentes(models.Model):
    nome = models.CharField(max_length=40)
    paises = models.ForeignKey(Pais,on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.nome} {self.paises}'
    
class Estados(models.Model):
    nome = models.CharField(max_length=30)
    area = models.CharField(max_length=30)
    temperatura = models.CharField(max_length=20)
    
    def __str__(self):
        return f'{self.nome} {self.area}'

class Temperatura(models.Model):
    graus = models.DecimalField(max_digits=3, decimal_places=2)
    fahrenheit = models.DecimalField(max_digits=3, decimal_places=2)
    
    def __str__(self):
        return f' {self.graus} {self.fahrenheit}'
    

class DadosClimaticos(models.Model):
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    clima = models.CharField(max_length=30)
    graus = models.ForeignKey(Temperatura, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.pais
    

    