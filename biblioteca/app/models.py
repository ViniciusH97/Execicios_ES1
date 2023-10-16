from django.db import models

# Create your models here.
    
class Genero(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Autor(models.Model):
    nome = models.CharField(max_length=50)
    site = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    genero = models.ForeignKey(Genero,on_delete=models.CASCADE)

    def __str__(self):
        return self.site
    
    def __str__(self):
        return self.cidade
    
    def __str__(self):
        return f'{self.genero} {self.nome}'

    def __str__(self):
        return self.nome

class Editora(models.Model):
    nome = models.CharField(max_length=50)
    site = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    
    def __str__(self):
        return self.site
    
    def __str__(self):
        return self.nome

class Livro(models.Model):
    nome = models.CharField(max_length=50)
    autor = models.ForeignKey(Autor,on_delete=models.CASCADE)
    editora = models.ForeignKey(Editora,on_delete=models.CASCADE)
    genero = models.ManyToManyField(Genero)
    preco = models.DecimalField(max_digits= 5, decimal_places=2)
    data_plub = models.DateTimeField()
    status =  models.BooleanField(default=False) 

    def __str__(self):
        return f'{self.editora} {self.nome}'
    
    def __str__(self):
        return f'{self.autor} {self.nome}'

    def __str__(self):
        return f'{self.genero} {self.nome}'

    def __str__(self):
        return self.nome

class Cidade(models.Model):
    nome = models.CharField(max_length=50)
    UF = models.CharField(max_length=20)

    def __str__(self):
        return self.UF

    def __str__(self):
        return self.nome

    
class Leitor(models.Model):
    nome = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11)

    def __str__(self):
        return self.email
    
    def __str__(self):
        return self.cpf
    
    def __str__(self):
        return self.nome


class Emprestimo(models.Model):
    nome = models.CharField(max_length=30)
    livro = models.ForeignKey(Livro,on_delete=models.CASCADE)
    leitor = models.ForeignKey(Leitor,on_delete=models.CASCADE)
    data_emprestimo = models.DateField(default='2023-09-14')
    data_de_devolucao = models.DateTimeField()

    def __str__(self):
        return f'{self.autor} {self.nome}'

    def __str__(self):
        return f'{self.livro} {self.nome}'
    
    def __str__(self):
        return f'{self.leitor} {self.nome}'

    def __str__(self):
        return self.nome
    

   