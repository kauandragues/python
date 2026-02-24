from django.shortcuts import render
from django.views.generic import ListView
from .models import Aluno

# Create your views here.
class AlunoListView(ListView):
    model = Aluno
    template_name = "aluno_list.html"
    context_object_name = "alunos"
    paginate_by = 30

    def get_queryset(self):
        return Aluno.objects.select_related("sala").all()

