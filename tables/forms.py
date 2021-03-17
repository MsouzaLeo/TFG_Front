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
            'cod_natureza_exame': 'Natureza de Exame da Especie'
        }

    def __init__(self, *arg, **kwargs):
        super(EspecieForm, self).__init__(*arg, **kwargs)
        self.fields['cod_natureza_exame'].empty_label = 'Selecione'
        self.fields['sigla'].required = False
