from django.shortcuts import render
from . models  import*

def matricula(request):
    matriculas = {
         'matriculas':Matricula.objects.all()
    }
    
    return render(request,'consulta/matricula.html', matriculas)

def curso(request):
    curso = {
        'curso':Curso.objects.all()
    }
    
    return render(request,'consulta/curso.html',curso)

def instituicao(request):
    instituicao = {
        'instituicao': Instituicao.objects.all()
    }
    
    return render(request, 'consulta/instituicao.html', instituicao)

def ocupacao(request):
    ocupacao = {
        'ocupacao': Ocupacao.objects.all()
    }
    
    return render(request, 'consulta/ocupacao.html', ocupacao)