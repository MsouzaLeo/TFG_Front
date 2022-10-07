from django import forms
from .models import *


class EspecieForm(forms.ModelForm):

    class Meta:
        model = EspecieModel
        fields = ('cod_especie_exame', 'descricao_especie',
                  'sigla', 'cod_natureza_exame')
        labels = {
            'cod_especie_exame': 'Código da Especie',
            'descricao_especie': 'Descrição da Especie',
            'sigla':'Classificação',
            'cod_natureza_exame': 'Natureza de Exame da Especie'
        }

    def __init__(self, *arg, **kwargs):
        super(EspecieForm, self).__init__(*arg, **kwargs)
        self.fields['cod_natureza_exame'].empty_label = 'Selecione'
        self.fields['sigla'].required = True


class NaturezaForm(forms.ModelForm):
    class Meta:
        model = NaturezaModel
        fields = ('cod_natureza_exame', 'descricao_natureza', 'ciencia')
        labels = {
            'cod_natureza_exame': 'Código da Natureza',
            'descricao_natureza': 'Descrição da Natureza',
            'ciecia': 'Ciência'
        }

        def __init__(self, *arg, **kwargs):
            super(NaturezaForm, self).__init__(*arg, **kwargs)


class PeritoForm(forms.ModelForm):
    class Meta:
        model = PeritoModel
        fields = ('masp', 'nome_perito')
        labels = {
            'masp': 'MASP de Matrícula',
            'nome_perito': 'Nome do Perito'
        }

        def __init__(self, *arg, **kwargs):
            super(PeritoForm, self).__init__(*arg, **kwargs)


class UniexaForm(forms.ModelForm):
    class Meta:
        model = UniexaModel
        fields = ('cod_unidade_exame', 'comarca_da_unidade')
        labels = {
            'cod_unidade_exame': 'Código da Unidade de Exame',
            'comarca_da_unidade': 'Comarca da Unidade de Exame'
        }

        def __init__(self, *arg, **kwargs):
            super(UniexaForm, self).__init__(*arg, **kwargs)


class UniresForm(forms.ModelForm):
    class Meta:
        model = UniresModel
        fields = ('cod_unidade_requisitante', 'unidade',
                  'tipo_unidade', 'subordinacao', 'geocodigo')
        labels = {
            'cod_unidade_requisitante': 'Código da Unidade Requisitante',
            'unidade': 'Nome da Unidade',
            'tipo_unidade': 'Tipo de Unidade',
            'subordinacao': 'Subordinação',
            'geocodigo': 'Município'
        }

        def __init__(self, *arg, **kwargs):
            super(UniresForm, self).__init__(*arg, **kwargs)


class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = DepartamentoModel
        fields = ('cod_departamento', 'departamento')
        labels = {
            'cod_departamento': 'Código do Departamento',
            'departamento': 'Nome do Departamento'
        }

        def __init__(self, *arg, **kwargs):
            super(DepartamentoForm, self).__init__(*arg, **kwargs)
            self.fields['departamento'].required = True

class RegionalForm(forms.ModelForm):
    class Meta:
        model = RegionalModel
        fields = ('cod_regional', 'regional', 'cod_departamento')
        labels = {
            'cod_regional': 'Código da Regional',
            'regional': 'Nome da Regional',
            'cod_departamento': 'Departamento',
        }

        def __init__(self, *arg, **kwargs):
            super(RegionalForm, self).__init__(*arg, **kwargs)
            self.fields['regional'].required = True


class MunicipioForm(forms.ModelForm):
    class Meta:
        model = MunicipioModel
        fields = ('geocodigo', 'municipio', 'cod_regional')
        labels = {
            'geocodigo': 'Geocódigo do Município',
            'municipio': 'Nome do Município',
            'cod_regional': 'Regional',
        }

        def __init__(self, *arg, **kwargs):
            super(MunicipioForm, self).__init__(*arg, **kwargs)
            self.fields['municipio'].required = True