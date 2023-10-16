from django.db import models
from app.models import *

class Cidade(models.Model):
    nome = models.CharField(max_length=20)
    uf = models.CharField(max_length=2)

    def __str__(self):
        return self.nome

class Pessoa(models.Model):
    nome = models.CharField(max_length=50)
    pai = models.CharField(max_length=20)
    mae = models.CharField(max_length=20)
    cpf = models.CharField(max_length=11)
    email = models.CharField(max_length=30)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Ocupacao(models.Model):
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome

class Area(models.Model):
    nome = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

class Periodo_de_curso(models.Model):
    periodo = models.CharField(max_length=15)

    def __str__(self):
        return self.periodo

class Disciplina(models.Model):
    nome = models.CharField(max_length=30)
    area_saber = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
    
class Instituicao(models.Model):
    nome = models.CharField(max_length=50)
    site = models.CharField(max_length=30)
    tel = models.CharField(max_length=14)
    
    def __str__(self):
        return self.nome
    

class Curso(models.Model):
    nome = models.CharField(max_length=50)
    carga_horaria_total = models.IntegerField()
    duracao_meses = models.IntegerField()
    area_saber = models.ForeignKey(Area, on_delete=models.CASCADE)
    instituicao = models.CharField(max_length=50)
    periodo = models.ForeignKey(Periodo_de_curso, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Matricula(models.Model):
    instituicao = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='matriculas_instituicao')
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='matriculas_curso')
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    data_inicio = models.DateTimeField()
    data_previsao_termino = models.DateTimeField()

    def __str__(self):
        return f'{self.instituicao} {self.pessoa} {self.curso} {self.data_inicio} {self.data_previsao_termino}'

class Avaliacoe(models.Model):
    descricao = models.CharField(max_length=50)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.disciplina} {self.curso} {self.descricao}'

class Frequencia(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    numero_faltas = models.IntegerField()

    def __str__(self):
        return f'{self.disciplina} {self.curso} {self.numero_faltas}'

class Turno(models.Model):
    turno = models.CharField(max_length=10)
    nome = models.CharField(max_length=10)
    semestre = models.ForeignKey(Periodo_de_curso, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.semestre} {self.turno} {self.nome}'

class Ocorrencia(models.Model):
    descricao = models.CharField(max_length=50)
    data = models.DateTimeField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.disciplina} {self.curso} {self.pessoa} {self.descricao}'

class Manter_disciplina(models.Model):
    nome = models.CharField(max_length=20)
    carga_horaria = models.DecimalField(max_digits=3, decimal_places=2)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    periodo = models.ForeignKey(Periodo_de_curso, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.curso} {self.periodo} {self.nome} {self.carga_horaria}'

class Manter_tipo_de_avaliacao(models.Model):
    prova = models.CharField(max_length=50)
    trabalho = models.CharField(max_length=50)
    projeto = models.CharField(max_length=50)
    lista_de_exercicio = models.CharField(max_length=50)

    def __str__(self):
        return self.prova

    def __str__(self):
        return self.trabalho

    def __str__(self):
        return self.projeto

    def __str__(self):
        return self.lista_de_exercicio
