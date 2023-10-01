from django.urls import path
from Budget.views import orcamento, suporte, calculadoraSolar, informacoes
from Budget.views import sobreNos, empresas

urlpatterns = [
    path('', orcamento),  # Orçamento
    path('calculadoraSolar/', calculadoraSolar),  # Calculadora Solar
    path('suporte/', suporte),  # Contato
    path('informacoes/', informacoes),  # Informações
    path('sobreNos/', sobreNos),  # Sobre Nós
    path('empresas/', empresas),  # Empresas Próximas A Mim
]
