
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
    def clean_nome(self):
        nome = self.cleaned_data.get('nome','').strip()
        if not nome:
            raise forms.ValidationError('O nome do aluno não pode ficar vazio.')
        if len(nome) < 3:
            raise forms.ValidationError('O nome deve ter ao menos 3 caracteres.')
        return nome
