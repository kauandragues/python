from django.contrib import admin
from .models import Sala, Aluno, Materia, Nota

# Register your models here.
@admin.register(Sala)
class SalaAdmin(admin.ModelAdmin):
    list_display = ("nome", "ano")
    search_fields = ("nome",)
    ordering = ("nome",)

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ("nome", "sala")
    search_fields = ("nome",)
    list_filter = ("sala",)
    raw_id_fields = ("sala",)

@admin.register(Materia)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    search_fields = ("nome",)

@admin.register(Nota)
class NotaAdmin(admin.ModelAdmin):
    list_display = ("aluno", "materia", "nota")
    search_fields = ("nota",)
    list_filter = ("aluno",)
    ordering = ("materia",)
