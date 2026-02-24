from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import AlunoForm
from .models import Aluno

# Create your views here.
def listar_alunos(request):
    alunos = Aluno.objects.all()
    return render(request, 'escola/aluno/lista_alunos.html', {'alunos': alunos})

def cadastrar_aluno(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_aluno')
    else:
        form = AlunoForm()

    return render(request, 'escola/aluno/cadastra_alunos.html', {'form': form})

def editar_aluno(request):

def index(request):
    return HttpResponse("index")