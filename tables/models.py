from django.db import models


class NaturezaModel(models.Model):
    cod_natureza_exame = models.IntegerField(primary_key=True)
    descricao_natureza = models.CharField(max_length=70)
    ciencia = models.CharField(max_length=30)

    def __str__(self):
        return self.descricao_natureza

    class Meta:
        db_table = "natureza_exame"


class EspecieModel(models.Model):
    cod_especie_exame = models.IntegerField(primary_key=True)
    descricao_especie = models.CharField(max_length=150)
    cod_natureza_exame = models.ForeignKey(
        'NaturezaModel', on_delete=models.DO_NOTHING, db_column='cod_natureza_exame')
    sigla = models.CharField(max_length=3)

    class Meta:
        db_table = "especie_exame"


class PeritoModel(models.Model):
    masp = models.IntegerField(primary_key=True)
    nome_perito = models.CharField(max_length=70)

    class Meta:
        db_table = "perito_responsavel"


class UniexaModel(models.Model):
    cod_unidade_exame = models.CharField(max_length=6, primary_key=True)
    comarca_da_unidade = models.CharField(max_length=70)

    class Meta:
        db_table = "unidade_exame"


class UniresModel(models.Model):
    cod_unidade_requisitante = models.CharField(max_length=6, primary_key=True)
    unidade = models.CharField(max_length=70)
    tipo_unidade = models.CharField(max_length=50)
    subordinacao = models.CharField(max_length=100)
    municipio = models.CharField(max_length=80)
    geocodigo = models.IntegerField()

    class Meta:
        db_table = "unidade_requisitante"
