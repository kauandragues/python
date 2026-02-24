
from django.urls import path
from . import views
urlpatterns = [
    path('salas/', views.listar_salas, name='listar_salas'),
    path('salas/nova/', views.criar_sala, name='criar_sala'),
    path('salas/editar/<int:id>/', views.editar_sala, name='editar_sala'),
    path('salas/excluir/<int:id>/', views.deletar_sala, name='deletar_sala'),
    path('alunos/', views.listar_alunos, name='listar_alunos'),
    path('alunos/novo/', views.criar_aluno, name='criar_aluno'),
    path('alunos/editar/<int:id>/', views.editar_aluno, name='editar_aluno'),
    path('alunos/excluir/<int:id>/', views.deletar_aluno, name='deletar_aluno'),
]
