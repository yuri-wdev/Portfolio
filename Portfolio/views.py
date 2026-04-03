from django.shortcuts import render
from django.http import HttpResponse


def Sobre(request):
    return render(request, 'Main.html')

def Contato(request):
    return render(request, 'Contato.html')

def Projetos(request):
    return render(request, 'Projetos.html')