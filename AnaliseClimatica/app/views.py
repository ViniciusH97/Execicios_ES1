from django.shortcuts import render, redirect
from app.forms import *
from . models import *
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from urllib.parse import unquote

def consultar_paises(request):  # replace with your actual view function name
    paises = Pais.objects.all()  # replace Pais with your actual model name
    return render(request, 'paises/paises.html', {'paises': paises})


def adm(request):
    return render(request, 'adm/adm.html')


def consultar_causa(request):
    return render(request, 'causa/consultar_causa.html')


def buscar_causas(request):
    estado_nome = request.GET.get('estado_id')
    estado_nome_decoded = unquote(estado_nome)
    estado = get_object_or_404(Estado, nome=estado_nome_decoded)
    
    mapa_brasil_src = f'/static/mapa_brasil.jpeg'

    causas = estado.causas.all()


    data = {'causas': [causa.to_dict_json() for causa in causas], 'mapa_brasil_src': mapa_brasil_src}
    return JsonResponse(data)

def mostrar_dados(request):
    estados = Estado.objects.all()
    dados_estado = None

    if request.method == 'GET':
        estado_nome = request.GET.get('estado')
        if estado_nome:
            dados_estado = get_object_or_404(Estado, nome=estado_nome)

    context = {
        'estados': estados,
        'dados_estado': dados_estado
    }

    return render(request, 'index.html', context)

def index(request):
    estados = Estado.objects.all()
    dados_estado = None

    if request.method == 'GET':
        estado_nome = request.GET.get('estado_id')
    if estado_nome:
        dados_estado = Estado.objects.get(nome=estado_nome)


    context = {
        'estados': estados,
        'dados_estado': dados_estado
    }

    return render(request, 'index.html', context)
