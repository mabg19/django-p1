from django.urls import path
from Budget.views import orcamento, suporte, calculadoraSolar, home
from Budget.views import sobreNos, empresas, area

urlpatterns = [
    path('', orcamento),  # Orçamento
    path('area/', area),  # Área Disponível
    path('calculadoraSolar/', calculadoraSolar),  # Calculadora Solar
    path('suporte/', suporte),  # Contato
    path('informacoes/', home),  # Informações
    path('sobreNos/', sobreNos),  # Sobre Nós
    path('empresas/', empresas),  # Empresas Próximas A Mim
]
