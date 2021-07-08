from django.db import models


class NaturezaModel(models.Model):
    cod_natureza_exame = models.IntegerField(primary_key=True)
    descricao_natureza = models.CharField(max_length=70)
    ciencia = models.CharField(max_length=30)

    def __str__(self):
        return self.descricao_natureza

    class Meta:
        db_table = "natureza_exame"


SIGLAS = (
    ('', 'Selecione'),
    ('DI', 'DI'),
    ('DEA', 'DEA'),
    ('DEU', 'DEU')
)


class EspecieModel(models.Model):
    cod_especie_exame = models.IntegerField(primary_key=True)
    descricao_especie = models.CharField(max_length=150)
    cod_natureza_exame = models.ForeignKey(
        'NaturezaModel', on_delete=models.DO_NOTHING, db_column='cod_natureza_exame')
    sigla = models.CharField(max_length=3, choices=SIGLAS, default='')

    def __str__(self):
        return self.descricao_especie

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

    def __str__(self):
        return self.comarca_da_unidade

    class Meta:
        db_table = "unidade_exame"


class UniresModel(models.Model):
    cod_unidade_requisitante = models.CharField(max_length=6, primary_key=True)
    unidade = models.CharField(max_length=70)
    tipo_unidade = models.CharField(max_length=50)
    subordinacao = models.CharField(max_length=100)
    municipio = models.CharField(max_length=80)
    geocodigo = models.IntegerField()

    def __str__(self):
        return self.municipio

    class Meta:
        db_table = "unidade_requisitante"


class LaudoModel(models.Model):
    nmr_requisicao = models.CharField(max_length=15, primary_key=True)
    cod_natureza_exame = models.ForeignKey(
        'NaturezaModel', on_delete=models.DO_NOTHING, db_column='cod_natureza_exame')
    cod_especie_exame = models.ForeignKey(
        'EspecieModel', on_delete=models.DO_NOTHING, db_column='cod_especie_exame')
    cod_unidade_requisitante = models.ForeignKey(
        'UniresModel', on_delete=models.DO_NOTHING, db_column='cod_unidade_requisitante')
    cod_unidade_exame = models.ForeignKey(
        'UniexaModel', on_delete=models.DO_NOTHING, db_column='cod_unidade_exame')
    masp_perito = models.IntegerField()
    tipo_requisicao = models.CharField(max_length=20)
    nmr_procedimento = models.IntegerField()
    cod_modelo_laudo = models.IntegerField()
    data_requisicao_pericia = models.DateTimeField()
    data_distribuicao_requisicao = models.DateTimeField(blank=True, null=True)
    data_redistribuicao = models.DateTimeField(blank=True, null=True)
    data_devolucao_requisicao = models.DateTimeField(blank=True, null=True)
    data_aceite_requisicao = models.DateTimeField(blank=True, null=True)
    data_expedicao_laudo = models.DateTimeField(blank=True, null=True)
    tempo_confeccao_laudo = models.IntegerField()

    class Meta:
        db_table = 'laudo'
