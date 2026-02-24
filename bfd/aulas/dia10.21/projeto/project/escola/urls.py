from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('alunos/', views.listar_alunos, name='listar_alunos'),
    path('alunos/cadastrar', views.cadastrar_aluno, name='cadastrar_alunos'),
]
