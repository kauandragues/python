from django.db import models

# Create your models here.
class Sala (models.Model):
    nome = models.CharField("Nome da sala", max_length = 50, unique = True)
    capacidade = models.PositiveIntegerField("Capacidade", null = True, blank = True)
    descricao = models.TextField("Descrição", blank = True)

    class Meta:
        verbose_name = "Sala"
        verbose_name_plural = "Salas"
        ordering = ["nome"]

    def __str__(self):
        return self.nome

class Aluno (models.Model):
    nome = models.CharField("Nome", max_length = 120)
    matricula = models.CharField("Matricula", max_length = 30, unique = True)
    email = models.EmailField("E-mail", blank = True)
    data_nascimento = models.DateField("Data de nascimento", null = True, blank = True)
    
    #Relação alunos -> sala

    sala = models.ForeignKey(
        Sala,
        on_delete=models.SET_NULL,
        null = True,
        blank = True,
        related_name = "alunos",
        verbose_name = "Sala"
    )

    class Meta:
        verbose_name = "Aluno"
        verbose_name_plural = "Alunos"
        ordering =["nome"]

    def __str__(self):
        return f"{self.nome} ({self.matricula})"


