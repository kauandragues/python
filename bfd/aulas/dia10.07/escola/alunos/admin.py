from django.contrib import admin
from .models import Aluno, Sala

# Register your models here.
@admin.register(Sala)
class SalaAdmin(admin.ModelAdmin):
    list_display = ("nome", "capacidade")
    search_fields = ("nome",)
    ordering = ("nome",)

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ("nome", "matricula", "sala", "email")
    search_fields = ("nome", "matricula", "email")
    list_filter = ("sala",)
    raw_id_fields = ("sala",)
