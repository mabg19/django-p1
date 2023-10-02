from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def orcamento(request):
    return render(request, 'global/orcamento.html', context={
        'name': 'Cálculo Orçamento'
    })


def calculadoraSolar(request):
    return HttpResponse('Calculadora Solar')


def area(request):
    return render(request, 'global/area.html', context={
        'name': 'Área Disponível'
    })


def suporte(request):
    return HttpResponse('Suporte')


def home(request):
    return render(request, 'global/home.html', context={
        'name': 'Cálculo Orçamento'
    })


def sobreNos(request):
    return HttpResponse('Sobre Nós')


def empresas(request):
    return HttpResponse('Empresas Próximas A Mim')
