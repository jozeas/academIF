from django.shortcuts import render
from . models import *

def membro(request):
    membros = {
        'membros': Membro.objects.all()
    }
    return render(request, 'membro.html', membros)

def registroaula(request):
    registroaulas = {
        'registroaulas': Registroaula.objects.all()
    }
    return render(request, 'registroaula.html', registroaulas)

def treinamento(request):
    treinamentos = {
        'treinamentos': Treinamento.objects.all()
    }
    return render(request, 'treinamento.html', treinamentos)
def treinador(request):
    consultas = {
        'consultas': Treinador.objects.all()
    }
    return render(request, 'registroaula.html', consultas)