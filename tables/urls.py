from django.urls import path

from . import views

urlpatterns = [
     path('', views.home, name='dash'),
     path('unires/', views.uniresList, name='unires-list'),
     path('uniexa/', views.uniexaList, name='uniexa-list'),
     path('perito/', views.peritoList, name='perito-list'),
     path('natureza/', views.naturezaList, name='natureza-list'),
     path('especie/', views.especieList, name='especie-list'),
     path('departamento/', views.departamentoList, name='departamento-list'),
     path('regional/', views.regionalList, name='regional-list'),
     path('municipio/', views.municipioList, name='municipio-list'),

     path('municipio/novoMunicipio/', views.municipioCreate, name='novo-municipio'),
     path('regional/novaRegional/', views.regionalCreate, name='novo-regional'),
     path('departamento/novoDepartamento/', views.departamentoCreate, name='novo-departamento'),
     path('especie/novaEspecie/', views.especieCreate, name='nova-especie'),
     path('natureza/novaNatureza/', views.naturezaCreate, name='nova-natureza'),
     path('perito/novoPerito/', views.peritoCreate, name='novo-perito'),
     path('uniexa/novaUniexa/', views.uniexaCreate, name='nova-uniexa'),
     path('unires/novaUnires/', views.uniresCreate, name='nova-unires'),

     path('municipio/<int:geocodigo>/', views.municipioEdit, name='municipio-update'),
     path('regional/<int:cod_regional>/', views.regionalEdit, name='regional-update'),
     path('departamento/<int:cod_departamento>/', views.departamentoEdit, name='departamento-update'),
     path('especie/<int:cod_especie_exame>/', views.especieEdit, name='especie-update'),
     path('natureza/<int:cod_natureza_exame>/', views.naturezaEdit, name='natureza-update'),
     path('perito/<int:masp>/', views.peritoEdit, name='perito-update'),
     path('uniexa/<str:cod_unidade_exame>/', views.uniexaEdit, name='uniexa-update'),
     path('unires/<str:cod_unidade_requisitante>/', views.uniresEdit, name='unires-update'),

     path('upload/', views.upload, name='upload'),
     path('ETL/', views.run_python_script, name='upload'),

     path('relatorio-especie/', views.relatorio_especie),
     path('relatorio-natureza/', views.relatorio_natureza),
     path('relatorio-perito/', views.relatorio_perito),
     path('relatorio-unidadex/', views.relatorio_unidadex),
     path('relatorio-unidader/', views.relatorio_unidader),

     path('ad-hoc/', views.adhoc, name='adhoc'),

     path('dadosMapa/', views.dadosMapa, name='teste'),
     path('dadosGraf/<int:geocod>/', views.dadosLinha, name='teste'),
     path('dadosGrafRegional/<int:regional>/', views.dadosLinhaRegional, name='teste'),
     path('dadosGrafDepartamento/<int:departamento>/', views.dadosLinhaDepartamento, name='teste'),

     path('dash/', views.dash, name='dash'),
]
