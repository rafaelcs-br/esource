from django.db import models

# Create your models here.
class Status(models.TextChoices):
    DISPONIVEL = 'DIS', 'Disponível'
    INDISPONIVEL = 'IND', 'Indisponível'

class UF(models.TextChoices):
    AC = 'AC', 'Acre'
    AL = 'AL', 'Alagoas'
    AP = 'AP', 'Amapá'
    AM = 'AM', 'Amazonas'
    BA = 'BA', 'Bahia'
    CE= 'CE', 'Ceará'
    DF = 'DF', 'Distrito Federal'
    ES = 'ES', 'Espírito Santo'
    GO = 'GO', 'Goiás'
    MA = 'MA', 'Maranhão'
    MT = 'MT', 'Mato Grosso'
    MS = 'MS', 'Mato Grosso do Sul'
    MG = 'MG', 'Minas Gerais'
    PA = 'PA', 'Pará'
    PB = 'PB', 'Paraíba'
    PR = 'PR', 'Paraná'
    PE = 'PE', 'Pernambuco'
    PI = 'PI', 'Piauí'
    RJ = 'RJ', 'Rio de Janeiro'
    RN = 'RN', 'Rio Grande do Norte'
    RS = 'RS', 'Rio Grande do Sul'
    RO = 'RO', 'Rondônia'
    RR = 'RR', 'Roraima'
    SC = 'SC', 'Santa Catarina'
    SP = 'SP', 'São Paulo'
    SE = 'SE', 'Sergipe'
    TO = 'TO', 'Tocantins'

class Evento(models.Model):
    nome = models.CharField(max_length=150)
    sigla = models.CharField(max_length=50)
    data_realizacao = models.DateField()
    link = models.URLField(blank=True, null=True)
    status = models.CharField(max_length=3, choices=Status.choices, default=Status.DISPONIVEL)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"
        ordering = ['-data_realizacao']

    def __str__(self):
        return f"{self.sigla} - {self.nome}"

class Autor(models.Model):
    nome = models.CharField(max_length=255)
    citacao = models.CharField(max_length=255, help_text='EX.: Santos, R.')
    instituicao = models.CharField(max_length=255)
    unidade_federativa = models.CharField(max_length=2, choices=UF.choices)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Autores"

    def __str__(self):
        return self.nome

class Subarea(models.Model):
    nome = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = "Subárea"
        verbose_name_plural = "Subáreas"

    def __str__(self):
        return self.nome

class Artigo(models.Model):
    titulo = models.CharField(max_length=255)
    data_publicacao = models.DateField(blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    material = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=3, choices=Status.choices, default=Status.DISPONIVEL)

    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name="artigos")
    autor = models.ManyToManyField(Autor, related_name='artigos')
    subareas = models.ManyToManyField(Subarea, related_name='artigos')

    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo