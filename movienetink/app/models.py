from django.db import models

class Genero(models. Model):
    acao = models.BooleanField()
    romance = models.BooleanField()
    suspense = models.BooleanField()
    cadastrar_genero  = models.CharField()

    def __str__(self):
        return f'{self.acao} {self.romance} {self.suspense} {self.cadastrar_genero}'

class Continente(models.Model):
    nome = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

class Gerenciar_paises(models.Model):
    nome = models.CharField(max_length=30)
    continente = models.ForeignKey(Continente,on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
    
class Gerenciar_atores_e_diretores(models.Model):
    nome = models.CharField(max_length=30)
    site = models.CharField(max_length=30)
    instagram = models.CharField(max_length=20)
    facebook = models.CharField(max_length=30)
    twitter = models.CharField(max_length=30)
    nacionalidade = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.nome} {self.site} {self.instagram} {self.facebook} {self.twitter} {self.nacionalidade}'
    

class Filme(models.Model):
    nome = models.CharField(max_length=45)
    duracao = models.CharField(max_length=5)
    sinopse = models.CharField(max_length=100)
    site_oficial = models.CharField(max_length=40)
    data_lancamento = models.DateField()
    nota_avaliacao = models.DecimalField(max_digits=2, decimal_places=2)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    pais = models.ForeignKey(Gerenciar_paises, on_delete=models.CASCADE)
    diretor = models.ForeignKey(Gerenciar_atores_e_diretores, on_delete=models.CASCADE)


class Gerenciar_com_atore(models.Model):
    filme = models.ForeignKey(Filme, on_delete=models.CASCADE)
    ator = models.ForeignKey(Gerenciar_atores_e_diretores, on_delete=models.CASCADE)    

    def __str__(self):
        return f'{self.filme} {self.ator}'
    
class Serie(models.Model):
    nome = models.CharField(max_length=45)
    duracao = models.CharField(max_length=5)
    sinopse = models.CharField(max_length=100)
    site_oficial = models.CharField(max_length=30)
    data_lancamento = models.DateField()
    nota_avaliacao = models.DecimalField(max_digits=2, decimal_places=2)
    genero = models.ForeignKey(Filme, on_delete=models.CASCADE)
    pais = models.ForeignKey(Gerenciar_paises, on_delete=models.CASCADE)
    diretor = models.ForeignKey(Gerenciar_atores_e_diretores, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.nome} {self.duracao} {self.sinopse} {self.site_oficial} {self.data_lancamento} {self.nota_avaliacao}'

class Gerenciar_episodio(models.Model):
    nome = models.CharField(max_length=45)
    duracao = models.CharField(max_length=5)
    data_disponibilizacao = models.DateField()

    def __str__(self):
        return f'{self.nome} {self.duracao} {self.data_disponibilizacao}'

class Gerenciar_temporadas(models.Model):
    temporada = models.CharField(max_length=10)

    def __str__(self):
        return self.temporada

class Gerenciar_serie_com_episodio(models.Model):
    serie = models.ForeignKey(Serie, on_delete=models.CASCADE)
    temporada = models.ForeignKey(Gerenciar_temporadas, on_delete=models.CASCADE)
    episodio = models.ForeignKey(Gerenciar_episodio, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.serie} {self.temporada} {self.episodio}'

    