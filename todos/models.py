from django.db import models

'''Criação da tabela do sqlite, importante para todo o código, black e null não são obrigatórios'''
class User(models.Model):
    nome = models.CharField(max_length=200, blank=False, null=False)
    idade = models.IntegerField() #caso seja um integerfield não se põe valor como o max_length
    data = models.DateTimeField(auto_now_add=True) #auto_now_add=True serve para preencher a data automaticamente
