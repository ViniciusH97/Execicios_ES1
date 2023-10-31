from django.shortcuts import render
from . models import *

def administracao(request):
    administracao = {
        'administracao':administracao.adm.all()
    }
    return render(request, 'administracao/adm.html'.adm)

def continentes(request):
    continentes = {
        'continentes':continentes.adm.all()
    }
    return render(request, 'continentes/continentes.html'.continentes)

def estados(request):
    estados = {
        'estados':estados.es.all()
    }
    return render(request, 'estados/estados.html'. estados)