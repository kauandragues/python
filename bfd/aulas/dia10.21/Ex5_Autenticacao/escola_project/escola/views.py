
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Sala, Aluno
from .forms import SalaForm, AlunoForm
def listar_salas(request):
    salas = Sala.objects.all().order_by('nome')
    return render(request, 'escola/salas_listar.html', {'salas': salas})

@login_required
def criar_sala(request):
    form = SalaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_salas')
    return render(request, 'escola/sala_form.html', {'form': form})
@login_required
def editar_sala(request, id):
    sala = get_object_or_404(Sala, id=id)
    form = SalaForm(request.POST or None, instance=sala)
    if form.is_valid():
        form.save()
        return redirect('listar_salas')
    return render(request, 'escola/sala_form.html', {'form': form})
@login_required
def deletar_sala(request, id):
    sala = get_object_or_404(Sala, id=id)
    if request.method == 'POST':
        sala.delete()
        return redirect('listar_salas')
    return render(request, 'escola/sala_confirm_delete.html', {'sala': sala})

def listar_alunos(request):
    alunos = Aluno.objects.all().order_by('nome')
    return render(request, 'escola/alunos_listar.html', {'alunos': alunos})

@login_required
def criar_aluno(request):
    form = AlunoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_alunos')
    return render(request, 'escola/aluno_form.html', {'form': form})
@login_required
def editar_aluno(request, id):
    aluno = get_object_or_404(Aluno, id=id)
    form = AlunoForm(request.POST or None, instance=aluno)
    if form.is_valid():
        form.save()
        return redirect('listar_alunos')
    return render(request, 'escola/aluno_form.html', {'form': form})
@login_required
def deletar_aluno(request, id):
    aluno = get_object_or_404(Aluno, id=id)
    if request.method == 'POST':
        aluno.delete()
        return redirect('listar_alunos')
    return render(request, 'escola/aluno_confirm_delete.html', {'aluno': aluno})
