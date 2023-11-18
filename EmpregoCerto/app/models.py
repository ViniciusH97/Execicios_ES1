from django.db import models

class Empresa(models.Model):
    nome = models.CharField(max_length=30)
    telefone = models.CharField(max_length=10)
    cpnj = models.DecimalField(max_digits=14, decimal_places=2)
    endereco = models.CharField(max_length=50)
    segmento = models.CharField(max_length=30)

    def __str__(self):
        return self.nome

class Login(models.Model):
    email = models.CharField(max_length=50)
    senha = models.CharField(max_length=20)

    def __str__(self):
        return self.email
    
class Usuario(models.Model):
    nome = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    telefone = models.CharField(max_length=10)
    endereco = models.CharField(max_length=40)
    login = models.ForeignKey(Login, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
    
class Vaga(models.Model):
    nome = models.CharField(max_length=30)
    descricao = models.CharField(max_length=50)
    salario = models.DecimalField(max_digits=14, decimal_places=2)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Candidato(models.Model):
    nome = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    telefone = models.CharField(max_length=10)
    endereco = models.CharField(max_length=40)
    vaga = models.ForeignKey(Vaga, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome