
from django import forms
from .models import Sala, Aluno
class SalaForm(forms.ModelForm):
    class Meta:
        model = Sala
        fields = ['nome', 'ano']
class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'sala']
