from django.db import models

# Create your models here.
class Sala(models.Model):
    nome = models.CharField(max_length=50)
    ano = models.IntegerField()

    def __str__(self):
        return self.nome

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE, related_name='alunos')

    def __str__(self):
        return self.nome

class Materia(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Nota(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name='notas')
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    nota = models.DecimalField(max_digits=4, decimal_places=2)