from django.db import models

class Pais(models.Model):
    nome = models.CharField(max_length=40)
    populacao = models.IntegerField()
    area = models.IntegerField()
    densidade = models.DecimalField(max_digits=4, decimal_places=2)
    capital = models.CharField(max_length=40)
    moeda = models.CharField(max_length=40)
    idioma = models.CharField(max_length=40)
    
    def __str__(self):
        return self.nome

class Continente(models.Model):
    nome = models.CharField(max_length=40)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome
    
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

class Causa(models.Model):
    nome = models.CharField(max_length=40)
    descricao = models.CharField(max_length=500)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    continente = models.ForeignKey(Continente, on_delete=models.CASCADE)
    estado = models.ForeignKey(Estado, related_name='causas', on_delete=models.CASCADE)
    
    def to_dict_json(self):
        return {
            'nome': self.nome,
            'descricao': self.descricao,
            'pais': self.pais.nome,
            'continente': self.continente.nome,
            'estado': self.estado.nome
        }
    
    def __str__(self):
        return self.nome
