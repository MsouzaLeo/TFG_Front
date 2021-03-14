from django.shortcuts import render
from tables.models import *


def especieList(request):
    showall = EspecieModel.objects.all()
    return render(request, 'especie/list.html', {"data": showall})


def naturezaList(request):
    showall = NaturezaModel.objects.all()
    return render(request, 'natureza/list.html', {"naturezas": showall})


def peritoList(request):
    showall = PeritoModel.objects.all()
    return render(request, 'perito/list.html', {"data": showall})


def uniexaList(request):
    showall = UniexaModel.objects.all()
    return render(request, 'uniexa/list.html', {"data": showall})


def uniresList(request):
    showall = UniresModel.objects.all()
    return render(request, 'unires/list.html', {"data": showall})
