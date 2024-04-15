from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.

def index_view(request):
    return render(request, "hello/index.html")


def saudacao_view(request, nome):

    context = {
        'nome': nome,
        'ano': 2024,
        }
    return render(request, "hello/saudacao.html", context)



def saudacao_idade_view(request, nome, idade):
    return HttpResponse(f"Olá {nome.capitalize()}, viva os {idade} anos!")
