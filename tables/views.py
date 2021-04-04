from subprocess import run, PIPE, Popen
import sys
from tkinter.constants import FALSE
from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.core.files.storage import FileSystemStorage
from tables.models import *
from .forms import *
import os
from scripts import *
import csv
import datetime


def especieList(request):
    search = request.GET.get('search')
    if search:
        showall = EspecieModel.objects.filter(
            descricao_especie__icontains=search)
    else:
        showall = EspecieModel.objects.all().order_by('cod_especie_exame')
    return render(request, 'especie/list.html', {"data": showall})


def export_csv(request):
    search = request.GET.get('search')
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="especies"' + \
        str(datetime.datetime.now())+'.csv'

    writer = csv.writer(response, delimiter=';')
    writer.writerow(
        ['Codigo da Especie', 'Descricao da Especie', 'Codigo da Natureza', 'Sigla'])

    if search:
        especies = EspecieModel.objects.filter(
            descricao_especie__icontains=search)
    else:
        especies = EspecieModel.objects.all().order_by('cod_especie_exame')

    for especie in especies:
        writer.writerow([str(especie.cod_especie_exame), str(especie.descricao_especie),
                         especie.cod_natureza_exame, especie.sigla])

    return response


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


def especieEdit(request, cod_especie_exame=0):
    if request.method == 'GET':
        if cod_especie_exame == 0:
            form = EspecieForm()
        else:
            especie = EspecieModel.objects.get(pk=cod_especie_exame)
            form = EspecieForm(instance=especie)
        return render(request, 'especie/edit.html', {'form': form})
    else:
        form = EspecieForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/especie')


def naturezaList(request):
    search = request.GET.get('search')
    if search:
        showall = NaturezaModel.objects.filter(
            descricao_natureza__icontains=search)
    else:
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


def naturezaEdit(request, cod_natureza_exame=0):
    if request.method == 'GET':
        if cod_natureza_exame == 0:
            form = NaturezaForm()
        else:
            natureza = NaturezaModel.objects.get(pk=cod_natureza_exame)
            form = NaturezaForm(instance=natureza)
        return render(request, 'natureza/edit.html', {'form': form})
    else:
        form = NaturezaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/natureza')


def peritoList(request):
    search = request.GET.get('search')
    if search:
        showall = PeritoModel.objects.filter(nome_perito__icontains=search)
    else:
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


def peritoEdit(request, masp=-1):
    if request.method == 'GET':
        if masp == -1:
            form = PeritoForm()
        else:
            perito = PeritoModel.objects.get(pk=masp)
            form = PeritoForm(instance=perito)
        return render(request, 'perito/edit.html', {'form': form})
    else:
        form = PeritoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/perito')


def uniexaList(request):
    search = request.GET.get('search')
    if search:
        showall = UniexaModel.objects.filter(
            comarca_da_unidade__icontains=search.upper())
    else:
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


def uniexaEdit(request, cod_unidade_exame=''):
    if request.method == 'GET':
        if cod_unidade_exame == '':
            form = UniexaForm()
        else:
            uniexa = UniexaModel.objects.get(pk=cod_unidade_exame)
            form = UniexaForm(instance=uniexa)
        return render(request, 'uniexa/edit.html', {'form': form})
    else:
        form = UniexaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/uniexa')


def uniresList(request):
    search = request.GET.get('search')
    # search.uppercase
    if search:
        showall = UniresModel.objects.filter(
            municipio__icontains=search.upper())
    else:
        showall = UniresModel.objects.all()
    return render(request, 'unires/list.html', {"data": showall})


def uniresCreate(request, cod_unidade_requisitante=''):
    if request.method == 'GET':
        if cod_unidade_requisitante == '':
            form = UniresForm()
        else:
            unires = UniresModel.objects.get(pk=cod_unidade_requisitante)
            form = UniresForm(instance=unires)
        return render(request, 'unires/create.html', {'form': form})
    else:
        form = UniresForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/unires')


def uniresEdit(request, cod_unidade_requisitante=''):
    if request.method == 'GET':
        if cod_unidade_requisitante == '':
            form = UniresForm()
        else:
            unires = UniresModel.objects.get(pk=cod_unidade_requisitante)
            form = UniresForm(instance=unires)
        return render(request, 'unires/edit.html', {'form': form})
    else:
        form = UniresForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/unires')


def upload(request):

    # run_python_script()
    return render((request), 'upload/upload.html')


def run_python_script(request):
    if request.method == 'POST':
        if len(request.FILES) != 0:
            uploaded_file = request.FILES['document']

            fs = FileSystemStorage()
            fs.save(uploaded_file.name, uploaded_file)

            out = run([sys.executable, 'scripts/ETL.py', 'media/' + uploaded_file.name],
                      shell=False, stdout=PIPE, stderr=PIPE)
            print(out.stdout.decode('utf-8'))
            os.remove(path='media/' + uploaded_file.name)
            return render(request, 'upload/upload.html', {"data": out.stdout.decode('utf-8')})
        else:
            return render(request, 'upload/upload.html')
