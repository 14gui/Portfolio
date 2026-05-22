from django.contrib import admin
from .models import Artigo, Like, Comentario

@admin.register(Artigo)
class ArtigoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'data_criacao')
    list_filter = ('autor',)
    search_fields = ('titulo', 'texto')

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('artigo', 'autor', 'data_criacao')

admin.site.register(Like)