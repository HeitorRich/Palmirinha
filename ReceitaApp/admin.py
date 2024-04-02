from django.contrib import admin
from ReceitaApp.models import Receita, Categoria

# Register your models here.
class ReceitaAdmin(admin.ModelAdmin):
    list_display = ["id", "nome", "categoria", "grau_de_dificuldade"]
    list_display_links = ["id", "nome"]
    list_filter = ["grau_de_dificuldade", "categoria"]
    search_fields = ["nome"]

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ["id", "nome"]
    list_display_link = ["id", "nome"]
    search_fields = ["nome"]


admin.site.register(Receita, ReceitaAdmin)
admin.site.register(Categoria, CategoriaAdmin)
