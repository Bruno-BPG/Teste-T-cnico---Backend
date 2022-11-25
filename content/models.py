from django.db import models

class Formulario_CNAB(models.Model):
    tipo = models.CharField(max_length=50)
    data = models.CharField(max_length=50)

    natureza = models.CharField(max_length=50)
    sinal = models.CharField(max_length=50)
    
    valor = models.CharField(max_length=50)
    cpf = models.CharField(max_length=50)
    cartao = models.CharField(max_length=50)
    hora = models.CharField(max_length=50)
    dono_nome = models.CharField(max_length=50)
    nome_loja = models.CharField(max_length=50)