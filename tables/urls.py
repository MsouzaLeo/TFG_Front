from django.urls import path

from . import views

urlpatterns = [
    path('unires/', views.uniresList, name='unires-list'),
    path('uniexa/', views.uniexaList, name='uniexa-list'),
    path('perito/', views.peritoList, name='perito-list'),
    path('natureza/', views.naturezaList, name='natureza-list'),
    path('especie/', views.especieList, name='especie-list'),
    path('especie/novaEspecie/', views.especieCreate, name='nova-especie'),
    path('natureza/novaNatureza/', views.naturezaCreate, name='nova-natureza'),
    path('perito/novoPerito/', views.peritoCreate, name='novo-perito'),
    path('uniexa/novaUniexa/', views.uniexaCreate, name='nova-uniexa'),
    path('unires/novaUnires/', views.uniresCreate, name='nova-unires'),
    path('especie/<int:cod_especie_exame>/',
         views.especieEdit, name='especie-update'),
    path('natureza/<int:cod_natureza_exame>/',
         views.naturezaEdit, name='natureza-update'),
    path('perito/<int:masp>/',
         views.peritoEdit, name='perito-update'),
    path('uniexa/<str:cod_unidade_exame>/',
         views.uniexaEdit, name='uniexa-update'),
    path('unires/<str:cod_unidade_requisitante>/',
         views.uniresEdit, name='unires-update'),
]

"""
TESTAR DEPOIS O UPDATE COM UMA NOVA VIEW SÓ PARA ELE, PARA NAO PODER EDITAR A PRIMARY KEY, SENÃO VAI DAR ERRO E VOU TER Q OUVIR DA VANESSA
É SÓ CRIAR UMA NOCA VIEW PARECIDO COM A DE CREATE, AI VC VOLTA A CREATE PRA COMO ELA TAVA ANTES, E NA DE EDIT DEIXA COMO ELA TA MAIS OU MENOS
E AI CRIAR UM HTML NOVO PRO EDIT, AI NAO COLOCA O CAMPO DA PRIMARY KEY NA PAGINA DE UPDATE
"""
