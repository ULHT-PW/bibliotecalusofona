from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello_view(request):
    context = {
        'nome': 'Manuel',
        'ano': 2024,
        }
    return render(request, 'app/index.html', context)


def sobre_view(request):
    return render(request, 'app/sobre.html')


def goodbye_view(request):
    nome = "Manuel"
    return HttpResponse(f"Adeus {nome}!")

def hello_name_view(request, nome):
    return HttpResponse(f"Olá {nome}!")
