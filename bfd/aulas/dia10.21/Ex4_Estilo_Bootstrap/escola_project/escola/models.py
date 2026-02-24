
from django.db import models
class Sala(models.Model):
    nome = models.CharField(max_length=50)
    ano = models.IntegerField()
    def __str__(self):
        return f"{self.nome} - {self.ano}"
class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE, related_name='alunos')
    def __str__(self):
        return self.nome
