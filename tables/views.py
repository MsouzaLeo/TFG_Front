from django.shortcuts import render, get_object_or_404, redirect
from tables.models import *
from .forms import *


def especieList(request):
    showall = EspecieModel.objects.all()
    return render(request, 'especie/list.html', {"data": showall})


def especieCreate(request):
    if request.method == 'GET':
        form = EspecieForm()
        return render(request, 'especie/create.html', {'form': form})
    else:
        form = EspecieForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect('/especie')


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
