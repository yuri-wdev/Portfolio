from django.shortcuts import render
from django.http import HttpResponse
from .models import Slide


def Sobre(request):
    return render(request, 'Main.html')

def Contato(request):
    return render(request, 'Contato.html')

def Projetos(request):
    slides = Slide.objects.filter(ativo=True)
    return render(request, 'Projetos.html', {'slides': slides})