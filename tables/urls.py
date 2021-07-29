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

     path('teste/<int:pk>', views.teste, name='teste'),

     path('dash/', views.dash, name='dash'),
]
