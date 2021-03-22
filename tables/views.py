from django.shortcuts import render, get_object_or_404, redirect
from tables.models import *
from .forms import *


def especieList(request):
    showall = EspecieModel.objects.all().order_by('cod_especie_exame')
    return render(request, 'especie/list.html', {"data": showall})


def especieCreate(request, cod_especie_exame=0):
    if request.method == 'GET':
        if cod_especie_exame == 0:
            form = EspecieForm()
        else:
            especie = EspecieModel.objects.get(pk=cod_especie_exame)
            form = EspecieForm(instance=especie)
        return render(request, 'especie/create.html', {'form': form})
    else:
        form = EspecieForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/especie')


def naturezaList(request):
    showall = NaturezaModel.objects.all().order_by('cod_natureza_exame')
    return render(request, 'natureza/list.html', {"data": showall})


def naturezaCreate(request, cod_natureza_exame=0):
    if request.method == 'GET':
        if cod_natureza_exame == 0:
            form = NaturezaForm()
        else:
            natureza = NaturezaModel.objects.get(pk=cod_natureza_exame)
            form = NaturezaForm(instance=natureza)
        return render(request, 'natureza/create.html', {'form': form})
    else:
        form = NaturezaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/natureza')


def peritoList(request):
    showall = PeritoModel.objects.all()
    return render(request, 'perito/list.html', {"data": showall})


def peritoCreate(request, masp=-1):
    if request.method == 'GET':
        if masp == -1:
            form = PeritoForm()
        else:
            perito = PeritoModel.objects.get(pk=masp)
            form = PeritoForm(instance=perito)
        return render(request, 'perito/create.html', {'form': form})
    else:
        form = PeritoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/perito')


def uniexaList(request):
    showall = UniexaModel.objects.all()
    return render(request, 'uniexa/list.html', {"data": showall})


def uniexaCreate(request, cod_unidade_exame=''):
    if request.method == 'GET':
        if cod_unidade_exame == '':
            form = UniexaForm()
        else:
            uniexa = UniexaModel.objects.get(pk=cod_unidade_exame)
            form = UniexaForm(instance=uniexa)
        return render(request, 'uniexa/create.html', {'form': form})
    else:
        form = UniexaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/uniexa')


def uniresList(request):
    showall = UniresModel.objects.all()
    return render(request, 'unires/list.html', {"data": showall})


def uniresCreate(request):
    if request.method == 'GET':
        form = UniresForm()
        return render(request, 'unires/create.html', {'form': form})
    else:
        form = UniresForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/unires')
