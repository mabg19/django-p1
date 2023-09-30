from django.urls import path
from Budget.views import home, contact, about


urlpatterns = [
    path('', home),  # Home
    path('sobre/', about),  # Sobre
    path('contato/', contact),  # Contato
]
