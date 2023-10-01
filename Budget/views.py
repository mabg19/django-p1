from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, 'global/home.html', context={
        'name': 'Maria Augusta'
    })


def calculadoraSolar(request):
    return HttpResponse('Calculadora Solar')


def suporte(request):
    return HttpResponse('Suporte')


def informacoes(request):
    return HttpResponse('Informações')


def sobreNos(request):
    return HttpResponse('Sobre Nós')


def empresas(request):
    return HttpResponse('Empresas Próximas A Mim')
