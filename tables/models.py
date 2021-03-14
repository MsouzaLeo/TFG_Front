from django.db import models


class EspecieModel(models.Model):
    cod_especie_exame = models.IntegerField()
    descricao_especie = models.CharField(max_length=150)
    cod_natureza_exame = models.IntegerField()
    sigla = models.CharField(max_length=3)

    class Meta:
        db_table = "especie_exame"


class NaturezaModel(models.Model):
    cod_natureza_exame = models.IntegerField()
    descricao_natureza = models.CharField(max_length=70)
    ciencia = models.CharField(max_length=30)

    class Meta:
        db_table = "natureza_exame"


class PeritoModel(models.Model):
    masp = models.IntegerField()
    nome_perito = models.CharField(max_length=70)

    class Meta:
        db_table = "perito_responsavel"


class UniexaModel(models.Model):
    cod_unidade_exame = models.CharField(max_length=6)
    comarca_da_unidade = models.CharField(max_length=70)

    class Meta:
        db_table = "unidade_exame"


class UniresModel(models.Model):
    cod_unidade_requisitante = models.CharField(max_length=6)
    unidade = models.CharField(max_length=70)
    tipo_unidade = models.CharField(max_length=50)
    subordinacao = models.CharField(max_length=100)
    municipio = models.CharField(max_length=80)
    geocodigo = models.IntegerField()

    class Meta:
        db_table = "unidade_requisitante"
