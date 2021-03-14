from django.urls import path

from . import views

urlpatterns = [
    path('unires/', views.uniresList, name='unires-list'),
    path('uniexa/', views.uniexaList, name='uniexa-list'),
    path('perito/', views.peritoList, name='perito-list'),
    path('natureza/', views.naturezaList, name='natureza-list'),
    path('especie/', views.especieList, name='especie-list'),
]
