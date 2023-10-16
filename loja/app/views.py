from django.shortcuts import render
from . models import *

# Create your views here.

def consulta(request):
    consultas = {
        'consultas': Produto.objects.all()
    }

    return render(request, 'consulta/consulta.html', consultas)