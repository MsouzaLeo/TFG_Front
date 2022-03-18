from subprocess import run, PIPE
import sys
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.db.models.aggregates import Count
from django.shortcuts import render,  redirect
from django.core.files.storage import FileSystemStorage
from tables.models import *
from .forms import *
import os
from django.http import JsonResponse
from scripts import *
import json
from django.db.models.functions import TruncMonth


def especieList(request):
    desc = request.GET.get('desc')
    sigla = request.GET.get('sigl')
    natureza = request.GET.get('natu')
    if desc or sigla or natureza:
        showall = EspecieModel.objects.filter(
            descricao_especie__icontains=desc, sigla__icontains=sigla, cod_natureza_exame__descricao_natureza__icontains=natureza)
    else:
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
            form.save(commit=True)
        return redirect('/especie')


def especieEdit(request, cod_especie_exame=0):
    if request.method == 'GET':
        if cod_especie_exame == 0:
            form = EspecieForm()
        else:
            especie = EspecieModel.objects.get(pk=cod_especie_exame)
            form = EspecieForm(instance=especie)
            form.fields['cod_especie_exame'].widget.attrs['readonly'] = True
        return render(request, 'especie/edit.html', {'form': form})
    else:
        especie = EspecieModel.objects.get(pk=cod_especie_exame)
        form = EspecieForm(request.POST, instance=especie)
        if form.is_valid():
            form.save(commit=True)
        else:
            print(request.POST)
        return redirect('/especie')


def naturezaList(request):
    desc = request.GET.get('desc')
    cien = request.GET.get('cien')
    if desc or cien:
        showall = NaturezaModel.objects.filter(
            descricao_natureza__icontains=desc, ciencia__icontains=cien)
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
            form.fields['cod_natureza_exame'].widget.attrs['readonly'] = True
        return render(request, 'natureza/edit.html', {'form': form})
    else:
        natureza = NaturezaModel.objects.get(pk=cod_natureza_exame)
        form = NaturezaForm(request.POST, instance=natureza)
        if form.is_valid():
            form.save(commit=True)
        else:
            print(request.POST)
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
            form.fields['masp'].widget.attrs['readonly'] = True
        return render(request, 'perito/edit.html', {'form': form})
    else:
        perito = PeritoModel.objects.get(pk=masp)
        form = PeritoForm(request.POST, instance=masp)
        if form.is_valid():
            form.save(commit=True)
        else:
            print(request.POST)
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
            form.fields['cod_unidade_exame'].widget.attrs['readonly'] = True
        return render(request, 'uniexa/edit.html', {'form': form})
    else:
        uniexa = UniexaModel.objects.get(pk=cod_unidade_exame)
        form = UniexaForm(request.POST,instance=cod_unidade_exame)
        if form.is_valid():
            form.save(commit=True)
        else:
            print(request.POST)
        return redirect('/uniexa')


def uniresList(request):
    search = request.GET.get('search')
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
            form.fields['cod_unidade_requisitante'].widget.attrs['readonly'] = True
        return render(request, 'unires/edit.html', {'form': form})
    else:
        unires = UniresModel.objects.get(pk=cod_unidade_requisitante)
        form = UniresForm(request.POST,instance=cod_unidade_requisitante)
        if form.is_valid():
            form.save(commit=True)
        else:
            print(request.POST)
        return redirect('/unires')


def upload(request):

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


def relatorio_especie(request):
    labels = []
    data = []
    teste = []
    limit = request.GET.get('Qtde')
    dataini = request.GET.get('dataini')
    datafim = request.GET.get('datafim')

    if limit == "Other":
        if request.GET.get('uma') != '':
            espe = int(request.GET.get('uma'))
        else:
            limit ="All"

    if (dataini and datafim):
        dataini = dataini + 'T00:00'
        datafim = datafim + 'T23:59'

    if (dataini and datafim) and limit == 'Ten':
        for especie in EspecieModel.objects.raw('''select l.cod_especie_exame ,n.descricao_especie, count(l.nmr_requisicao) as contagem 
            from laudo l inner join especie_exame n on l.cod_especie_exame = n.cod_especie_exame
            where l.data_requisicao_pericia BETWEEN %s AND %s
            group by n.cod_especie_exame, l.cod_especie_exame order by contagem desc LIMIT 10''',[dataini,datafim]):
            labels.append(especie.cod_especie_exame)
            data.append(especie.contagem)

    elif (dataini and datafim) and limit == 'Other':
        for especie in EspecieModel.objects.raw('''select l.cod_especie_exame ,n.descricao_especie, count(l.nmr_requisicao) as contagem 
            from laudo l inner join especie_exame n on l.cod_especie_exame = n.cod_especie_exame
            where l.data_requisicao_pericia BETWEEN %s AND %s AND n.cod_especie_exame = %s
            group by n.cod_especie_exame, l.cod_especie_exame order by contagem desc''',[dataini,datafim, espe]):
            labels.append(especie.cod_especie_exame)
            data.append(especie.contagem)

    elif not(dataini and datafim) and limit == 'Other':
        for especie in EspecieModel.objects.raw('''select l.cod_especie_exame ,n.descricao_especie, count(l.nmr_requisicao) as contagem 
            from laudo l inner join especie_exame n on l.cod_especie_exame = n.cod_especie_exame
            where n.cod_especie_exame = %s
            group by n.cod_especie_exame, l.cod_especie_exame order by contagem desc''',[espe]):
            labels.append(especie.cod_especie_exame)
            data.append(especie.contagem)

    elif not(dataini and datafim) and limit == 'Ten':
        for especie in EspecieModel.objects.raw('''select l.cod_especie_exame ,n.descricao_especie, count(l.nmr_requisicao) as contagem 
            from laudo l inner join especie_exame n on l.cod_especie_exame = n.cod_especie_exame
            group by n.cod_especie_exame, l.cod_especie_exame order by contagem desc LIMIT 10'''):
            labels.append(especie.cod_especie_exame)
            data.append(especie.contagem)

    elif (dataini and datafim) and limit == 'All':
        for especie in EspecieModel.objects.raw('''select l.cod_especie_exame ,n.descricao_especie, count(l.nmr_requisicao) as contagem
            from laudo l inner join especie_exame n on l.cod_especie_exame = n.cod_especie_exame
            where l.data_requisicao_pericia BETWEEN %s AND %s
            group by n.cod_especie_exame, l.cod_especie_exame order by contagem desc''',[dataini,datafim]):
            labels.append(especie.cod_especie_exame)
            data.append(especie.contagem)

    else:
        
        for especie in EspecieModel.objects.raw('''select l.cod_especie_exame ,n.descricao_especie, count(l.nmr_requisicao) as contagem
        from laudo l inner join especie_exame n on l.cod_especie_exame = n.cod_especie_exame
        group by n.cod_especie_exame, l.cod_especie_exame order by contagem desc'''):
            labels.append(especie.cod_especie_exame)
            teste.append(especie.descricao_especie)
            data.append(especie.contagem)


    context={
        'labels': json.dumps(labels),
        'data': data,
        'teste':teste
    }

    return render(request, 'relatorios/relatorio_especie.html', context)


def relatorio_natureza(request):
    labels = []
    data = []

    limit = 'All'
    limit = request.GET.get('Qtde')
    dataini = request.GET.get('dataini')
    datafim = request.GET.get('datafim')

    if limit == "Other":
        natu = str(request.GET.get('uma'))
        natu = '%' + natu + '%'

    if (dataini and datafim):
        dataini = dataini + 'T00:00'
        datafim = datafim + 'T23:59'
    
    if (dataini and datafim) and limit == 'Ten':
        for natureza in NaturezaModel.objects.raw('''select l.cod_natureza_exame ,n.descricao_natureza, count(l.nmr_requisicao) as contagem 
            from laudo l inner join natureza_exame n on l.cod_natureza_exame = n.cod_natureza_exame
            where l.data_requisicao_pericia BETWEEN %s AND %s
            group by n.cod_natureza_exame, l.cod_natureza_exame order by contagem desc LIMIT 10''',[dataini,datafim]):
            labels.append(natureza.descricao_natureza)
            data.append(natureza.contagem)

    elif (dataini and datafim) and limit == 'Other':
        for natureza in NaturezaModel.objects.raw("""select l.cod_natureza_exame ,n.descricao_natureza, count(l.nmr_requisicao) as contagem 
            from laudo l inner join natureza_exame n on l.cod_natureza_exame = n.cod_natureza_exame
            where (l.data_requisicao_pericia BETWEEN %s AND %s) AND n.descricao_natureza ILIKE  %s 
            group by n.cod_natureza_exame, l.cod_natureza_exame order by contagem desc""",[dataini,datafim,natu]):
            labels.append(natureza.descricao_natureza)
            data.append(natureza.contagem)

    elif not(dataini and datafim) and limit == 'Other':
        for natureza in NaturezaModel.objects.raw("""select l.cod_natureza_exame ,n.descricao_natureza, count(l.nmr_requisicao) as contagem 
            from laudo l inner join natureza_exame n on l.cod_natureza_exame = n.cod_natureza_exame
            where n.descricao_natureza ILIKE  %s 
            group by n.cod_natureza_exame, l.cod_natureza_exame order by contagem desc""",[natu]):
            labels.append(natureza.descricao_natureza)
            data.append(natureza.contagem)

    elif not(dataini and datafim) and limit == 'Ten':
        for natureza in NaturezaModel.objects.raw('''select l.cod_natureza_exame ,n.descricao_natureza, count(l.nmr_requisicao) as contagem 
            from laudo l inner join natureza_exame n on l.cod_natureza_exame = n.cod_natureza_exame
            group by n.cod_natureza_exame, l.cod_natureza_exame order by contagem desc LIMIT 10'''):
            labels.append(natureza.descricao_natureza)
            data.append(natureza.contagem)

    elif (dataini and datafim) and limit == 'All':
        for natureza in NaturezaModel.objects.raw('''select l.cod_natureza_exame ,n.descricao_natureza, count(l.nmr_requisicao) as contagem 
            from laudo l inner join natureza_exame n on l.cod_natureza_exame = n.cod_natureza_exame
            where l.data_requisicao_pericia BETWEEN %s AND %s
            group by n.cod_natureza_exame, l.cod_natureza_exame order by contagem desc''',[dataini,datafim]):
            labels.append(natureza.descricao_natureza)
            data.append(natureza.contagem)

    else:
        for natureza in NaturezaModel.objects.raw('''select l.cod_natureza_exame ,n.descricao_natureza, count(l.nmr_requisicao) as contagem 
        from laudo l inner join natureza_exame n on l.cod_natureza_exame = n.cod_natureza_exame
    group by n.cod_natureza_exame, l.cod_natureza_exame order by contagem desc'''):
            labels.append(natureza.descricao_natureza)
            data.append(natureza.contagem)

    context={
        'labels': json.dumps(labels),
        'data': data,
    }

    return render(request, 'relatorios/relatorio_natureza.html', context)


def relatorio_perito(request):
    labels = []
    data = []

    limit = request.GET.get('Qtde')
    dataini = request.GET.get('dataini')
    datafim = request.GET.get('datafim')

    if limit == "Other":
        if request.GET.get('uma') != '':
            masp = int(request.GET.get('uma'))
        else:
            limit ="All"

    if (dataini and datafim):
        dataini = dataini + 'T00:00'
        datafim = datafim + 'T23:59'

    if (dataini and datafim) and limit == 'Ten':
        for perito in PeritoModel.objects.raw('''select l.masp_perito,pe.masp, count(*) as contagem 
        from laudo l inner join perito_responsavel pe on l.masp_perito = pe.masp
        where l.data_requisicao_pericia BETWEEN %s AND %s
        group by pe.masp, l.masp_perito order by contagem desc LIMIT 10''',[dataini,datafim]):
            labels.append(perito.masp)
            data.append(perito.contagem)

    elif (dataini and datafim) and limit == 'Other':
        for perito in PeritoModel.objects.raw('''select l.masp_perito,pe.masp, count(*) as contagem 
        from laudo l inner join perito_responsavel pe on l.masp_perito = pe.masp
        where l.data_requisicao_pericia BETWEEN %s AND %s AND pe.masp = %s
        group by pe.masp, l.masp_perito order by contagem desc LIMIT 10''',[dataini,datafim, masp]):
            labels.append(perito.masp)
            data.append(perito.contagem)

    elif not(dataini and datafim) and limit == 'Other':
        for perito in PeritoModel.objects.raw('''select l.masp_perito,pe.masp, count(*) as contagem 
        from laudo l inner join perito_responsavel pe on l.masp_perito = pe.masp
        where pe.masp = %s
        group by pe.masp, l.masp_perito order by contagem desc LIMIT 10''',[masp]):
            labels.append(perito.masp)
            data.append(perito.contagem)

    elif not(dataini and datafim) and limit == 'Ten':
        for perito in PeritoModel.objects.raw('''select l.masp_perito,pe.masp, count(*) as contagem 
        from laudo l inner join perito_responsavel pe on l.masp_perito = pe.masp
        group by pe.masp, l.masp_perito order by contagem desc LIMIT 10'''):
            labels.append(perito.masp)
            data.append(perito.contagem)

    elif (dataini and datafim) and limit == 'All':
        for perito in PeritoModel.objects.raw('''select l.masp_perito,pe.masp, count(*) as contagem 
        from laudo l inner join perito_responsavel pe on l.masp_perito = pe.masp
        where l.data_requisicao_pericia BETWEEN %s AND %s
            group by pe.masp, l.masp_perito order by contagem desc''',[dataini,datafim]):
            labels.append(perito.masp)
            data.append(perito.contagem)

    else:
        for perito in PeritoModel.objects.raw('''select l.masp_perito,pe.masp, count(*) as contagem 
        from laudo l inner join perito_responsavel pe on l.masp_perito = pe.masp
            group by pe.masp, l.masp_perito order by contagem desc'''):
            labels.append(perito.masp)
            data.append(perito.contagem)

    context={
        'labels': json.dumps(labels),
        'data': data,
    }

    return render(request, 'relatorios/relatorio_perito.html', context)


def relatorio_unidadex(request):
    labels = []
    data = []

    limit = request.GET.get('Qtde')
    dataini = request.GET.get('dataini')
    datafim = request.GET.get('datafim')

    if limit == "Other":
        unid = str(request.GET.get('uma'))
        unid = '%' + unid + '%'

    if (dataini and datafim):
        dataini = dataini + 'T00:00'
        datafim = datafim + 'T23:59'

    if (dataini and datafim) and limit == 'Ten':
        for unidade in UniexaModel.objects.raw('''select l.cod_unidade_exame ,u.comarca_da_unidade as nome, count(l.nmr_requisicao) as contagem 
        from laudo l inner join unidade_exame u on l.cod_unidade_exame = u.cod_unidade_exame
        where l.data_requisicao_pericia BETWEEN %s AND %s
        group by u.cod_unidade_exame, l.cod_unidade_exame order by contagem desc LIMIT 10''',[dataini,datafim]):
            labels.append(unidade.nome)
            data.append(unidade.contagem)

    elif (dataini and datafim) and limit == 'Other':
        for unidade in UniexaModel.objects.raw('''select l.cod_unidade_exame ,u.comarca_da_unidade as nome, count(l.nmr_requisicao) as contagem 
        from laudo l inner join unidade_exame u on l.cod_unidade_exame = u.cod_unidade_exame
        where l.data_requisicao_pericia BETWEEN %s AND %s AND u.comarca_da_unidade ILIKE %s
        group by u.cod_unidade_exame, l.cod_unidade_exame order by contagem desc''',[dataini,datafim, unid]):
            labels.append(unidade.nome)
            data.append(unidade.contagem)

    elif not(dataini and datafim) and limit == 'Other':
        for unidade in UniexaModel.objects.raw('''select l.cod_unidade_exame ,u.comarca_da_unidade as nome, count(l.nmr_requisicao) as contagem 
        from laudo l inner join unidade_exame u on l.cod_unidade_exame = u.cod_unidade_exame
        where u.comarca_da_unidade ILIKE %s
        group by u.cod_unidade_exame, l.cod_unidade_exame order by contagem desc''',[unid]):
            labels.append(unidade.nome)
            data.append(unidade.contagem)

    elif not(dataini and datafim) and limit == 'Ten':
        for unidade in UniexaModel.objects.raw('''select l.cod_unidade_exame ,u.comarca_da_unidade as nome, count(l.nmr_requisicao) as contagem 
        from laudo l inner join unidade_exame u on l.cod_unidade_exame = u.cod_unidade_exame
        group by u.cod_unidade_exame, l.cod_unidade_exame order by contagem desc LIMIT 10'''):
            labels.append(unidade.nome)
            data.append(unidade.contagem)
    
    elif (dataini and datafim) and limit == 'All':
        for unidade in UniexaModel.objects.raw('''select l.cod_unidade_exame ,u.comarca_da_unidade as nome, count(l.nmr_requisicao) as contagem 
        from laudo l inner join unidade_exame u on l.cod_unidade_exame = u.cod_unidade_exame
        where l.data_requisicao_pericia BETWEEN %s AND %s
        group by u.cod_unidade_exame, l.cod_unidade_exame order by contagem desc''',[dataini,datafim]):
            labels.append(unidade.nome)
            data.append(unidade.contagem)

    else:
        for unidade in UniexaModel.objects.raw('''select l.cod_unidade_exame ,u.comarca_da_unidade as nome, count(l.nmr_requisicao) as contagem 
        from laudo l inner join unidade_exame u on l.cod_unidade_exame = u.cod_unidade_exame
        group by u.cod_unidade_exame, l.cod_unidade_exame order by contagem desc'''):
            labels.append(unidade.nome)
            data.append(unidade.contagem)

    context={
        'labels': json.dumps(labels),
        'data': data,
    }

    return render(request, 'relatorios/relatorio_unidadex.html', context)


def relatorio_unidader(request):
    labels = []
    data = []

    limit = request.GET.get('Qtde')
    dataini = request.GET.get('dataini')
    datafim = request.GET.get('datafim')

    if limit == "Other":
        unid = str(request.GET.get('uma'))
        unid = '%' + unid + '%'

    if (dataini and datafim):
        dataini = dataini + 'T00:00'
        datafim = datafim + 'T23:59'

    if (dataini and datafim) and limit == 'Ten':
        for unidade in UniresModel.objects.raw('''select l.cod_unidade_requisitante ,u.municipio as nome, count(l.nmr_requisicao) as contagem 
        from laudo l inner join unidade_requisitante u on l.cod_unidade_requisitante = u.cod_unidade_requisitante
        where l.data_requisicao_pericia BETWEEN %s AND %s
        group by u.cod_unidade_requisitante, l.cod_unidade_requisitante order by contagem desc LIMIT 10''',[dataini, datafim]):
            cod_nome = str(unidade.cod_unidade_requisitante +' - '+ unidade.nome)
            labels.append(cod_nome)
            data.append(unidade.contagem)
    
    elif (dataini and datafim) and limit == 'Other':
        for unidade in UniresModel.objects.raw('''select l.cod_unidade_requisitante ,u.municipio as nome, count(l.nmr_requisicao) as contagem 
        from laudo l inner join unidade_requisitante u on l.cod_unidade_requisitante = u.cod_unidade_requisitante
        where l.data_requisicao_pericia BETWEEN %s AND %s AND u.municipio ILIKE %s
        group by u.cod_unidade_requisitante, l.cod_unidade_requisitante order by contagem desc''',[dataini, datafim, unid]):
            cod_nome = str(unidade.cod_unidade_requisitante +' - '+ unidade.nome)
            labels.append(cod_nome)
            data.append(unidade.contagem)

    elif not(dataini and datafim) and limit == 'Other':
        for unidade in UniresModel.objects.raw('''select l.cod_unidade_requisitante ,u.municipio as nome, count(l.nmr_requisicao) as contagem 
        from laudo l inner join unidade_requisitante u on l.cod_unidade_requisitante = u.cod_unidade_requisitante
        where u.municipio ILIKE %s
        group by u.cod_unidade_requisitante, l.cod_unidade_requisitante order by contagem desc''',[unid]):
            cod_nome = str(unidade.cod_unidade_requisitante +' - '+ unidade.nome)
            labels.append(cod_nome)
            data.append(unidade.contagem)

    elif not(dataini and datafim) and limit == 'Ten':
        for unidade in UniresModel.objects.raw('''select l.cod_unidade_requisitante ,u.municipio as nome, count(l.nmr_requisicao) as contagem 
        from laudo l inner join unidade_requisitante u on l.cod_unidade_requisitante = u.cod_unidade_requisitante
        group by u.cod_unidade_requisitante, l.cod_unidade_requisitante order by contagem desc LIMIT 10'''):
            cod_nome = str(unidade.cod_unidade_requisitante +' - '+ unidade.nome)
            labels.append(cod_nome)
            data.append(unidade.contagem)

    elif (dataini and datafim) and limit == 'All':
        for unidade in UniresModel.objects.raw('''select l.cod_unidade_requisitante ,u.municipio as nome, count(l.nmr_requisicao) as contagem 
        from laudo l inner join unidade_requisitante u on l.cod_unidade_requisitante = u.cod_unidade_requisitante
        where l.data_requisicao_pericia BETWEEN %s AND %s
        group by u.cod_unidade_requisitante, l.cod_unidade_requisitante order by contagem desc''',[dataini, datafim]):
            cod_nome = str(unidade.cod_unidade_requisitante +' - '+ unidade.nome)
            labels.append(cod_nome)
            data.append(unidade.contagem)

    else:
        for unidade in UniresModel.objects.raw('''select l.cod_unidade_requisitante ,u.municipio as nome, count(l.nmr_requisicao) as contagem 
        from laudo l inner join unidade_requisitante u on l.cod_unidade_requisitante = u.cod_unidade_requisitante
        group by u.cod_unidade_requisitante, l.cod_unidade_requisitante order by contagem desc'''):
            cod_nome = str(unidade.cod_unidade_requisitante +' - '+ unidade.nome)
            labels.append(cod_nome)
            data.append(unidade.contagem)

    context={
        'labels': json.dumps(labels),
        'data': data,
    }

    return render(request, 'relatorios/relatorio_unidader.html', context)


def adhoc(request):
    natu = request.GET.get('natu')
    codnatu = request.GET.get('codnatu')
    espe = request.GET.get('espe')
    codespe = request.GET.get('codespe')
    classespe = request.GET.get('classespe')
    masp = request.GET.get('masp')
    unires = request.GET.get('unires')
    uniex = request.GET.get('uniex')
    tpres = request.GET.get('tpres')
    tipodata = request.GET.get('tipodata')
    dataini = ''
    datafim = ''
    if tipodata == "requisicao":
        dataini = request.GET.get('datainireq')
        datafim = request.GET.get('datafimreq')
    elif tipodata == "expedicao":
        dataini = request.GET.get('datainiexp')
        datafim = request.GET.get('datafimexp')

    if not(dataini and datafim):
        if natu or codnatu or espe or codespe or classespe or masp or unires or uniex or tpres:
            showall = LaudoModel.objects.filter(
                cod_natureza_exame__descricao_natureza__icontains=natu, cod_natureza_exame__cod_natureza_exame__icontains=codnatu, cod_especie_exame__descricao_especie__icontains=espe, cod_especie_exame__sigla__icontains=classespe, cod_especie_exame__cod_especie_exame__icontains=codespe, masp_perito__icontains=masp, cod_unidade_requisitante__municipio__icontains=unires, cod_unidade_exame__comarca_da_unidade__icontains=uniex, tipo_requisicao__icontains=tpres).order_by('nmr_requisicao')
        else:
            showall = LaudoModel.objects.all().order_by('nmr_requisicao')[:500]
    else:
        if tipodata == "requisicao":
            if natu or codnatu or espe or codespe or classespe or masp or unires or uniex or tpres or (dataini and datafim):
                showall = LaudoModel.objects.filter(
                    cod_natureza_exame__descricao_natureza__icontains=natu, cod_natureza_exame__cod_natureza_exame__icontains=codnatu, cod_especie_exame__descricao_especie__icontains=espe, cod_especie_exame__sigla__icontains=classespe, cod_especie_exame__cod_especie_exame__icontains=codespe, masp_perito__icontains=masp, cod_unidade_requisitante__municipio__icontains=unires, cod_unidade_exame__comarca_da_unidade__icontains=uniex, tipo_requisicao__icontains=tpres, data_requisicao_pericia__range=[dataini, datafim]).order_by('nmr_requisicao')
        elif tipodata == "expedicao":
            if natu or codnatu or espe or codespe or classespe or masp or unires or uniex or tpres or (dataini and datafim):
                showall = LaudoModel.objects.filter(
                    cod_natureza_exame__descricao_natureza__icontains=natu, cod_natureza_exame__cod_natureza_exame__icontains=codnatu, cod_especie_exame__descricao_especie__icontains=espe, cod_especie_exame__sigla__icontains=classespe, cod_especie_exame__cod_especie_exame__icontains=codespe, masp_perito__icontains=masp, cod_unidade_requisitante__municipio__icontains=unires, cod_unidade_exame__comarca_da_unidade__icontains=uniex, tipo_requisicao__icontains=tpres, data_expedicao_laudo__range=[dataini, datafim]).order_by('nmr_requisicao')
    
    p = Paginator(showall,2000)
    page = request.GET.get('page', 1)

    try:
        data = p.get_page(page)
        print(data.paginator.num_pages)
        print(data.number)
    except (EmptyPage, InvalidPage):
        data = p.page(p.num_pages)
    return render(request, 'relatorios/relatorio_adhoc.html', {'data':data})

def dash(request):
    natureza = NaturezaModel.objects.all().order_by('descricao_natureza')
    return render(request, 'dashboard/dash.html',{"data": natureza})

def home(request):
    return render(request, 'home.html')

def dadosMapa(request):
    natu = request.GET.get('natureza')
    inicio = request.GET.get('inicio')
    fim = request.GET.get('fim')
    if not natu and not inicio:
        data = LaudoModel.objects.values('cod_unidade_requisitante__geocodigo').annotate(value=Count('nmr_requisicao')).order_by('-value')
    elif natu and not(inicio and fim):
        data = LaudoModel.objects.values('cod_unidade_requisitante__geocodigo').annotate(value=Count('nmr_requisicao')).order_by('-value').filter(cod_natureza_exame=natu)
    elif not natu and (inicio and fim):
        data = LaudoModel.objects.values('cod_unidade_requisitante__geocodigo').annotate(value=Count('nmr_requisicao')).order_by('-value').filter(data_requisicao_pericia__range=[inicio, fim])
    elif natu and (inicio and fim):
        data = LaudoModel.objects.values('cod_unidade_requisitante__geocodigo').annotate(value=Count('nmr_requisicao')).order_by('-value').filter(cod_natureza_exame=natu, data_requisicao_pericia__range=[inicio, fim])
    return JsonResponse(list(data),safe=False)

def dadosLinha(request,geocod):
    natu = request.GET.get('natureza')
    inicio = request.GET.get('inicio')
    fim = request.GET.get('fim')
    if not natu and not inicio:
        data = LaudoModel.objects.annotate(mes_registro=TruncMonth('data_requisicao_pericia')).values('cod_unidade_requisitante__geocodigo','mes_registro').annotate(laudo_nmr=Count('nmr_requisicao')).order_by('mes_registro').filter(cod_unidade_requisitante__geocodigo__icontains=geocod)
    elif natu and not(inicio and fim):
        data = LaudoModel.objects.annotate(mes_registro=TruncMonth('data_requisicao_pericia')).values('cod_unidade_requisitante__geocodigo','mes_registro').annotate(laudo_nmr=Count('nmr_requisicao')).order_by('mes_registro').filter(cod_unidade_requisitante__geocodigo__icontains=geocod).filter(cod_natureza_exame=natu)
    elif not natu and (inicio and fim):
        data = LaudoModel.objects.annotate(mes_registro=TruncMonth('data_requisicao_pericia')).values('cod_unidade_requisitante__geocodigo','mes_registro').annotate(laudo_nmr=Count('nmr_requisicao')).order_by('mes_registro').filter(cod_unidade_requisitante__geocodigo__icontains=geocod).filter(data_requisicao_pericia__range=[inicio, fim])
    elif natu and (inicio and fim):
        data = LaudoModel.objects.annotate(mes_registro=TruncMonth('data_requisicao_pericia')).values('cod_unidade_requisitante__geocodigo','mes_registro').annotate(laudo_nmr=Count('nmr_requisicao')).order_by('mes_registro').filter(cod_unidade_requisitante__geocodigo__icontains=geocod).filter(data_requisicao_pericia__range=[inicio, fim], cod_natureza_exame=natu)
    return JsonResponse(list(data),safe=False)