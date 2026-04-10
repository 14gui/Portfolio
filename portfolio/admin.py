from django.contrib import admin
from .models import Licenciatura, Docente, UC, Projeto, Tecnologia, Competencia, Formacao, TFC

@admin.register(Licenciatura)
class LicenciaturaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ano_inicio')
    search_fields = ('nome',)

@admin.register(UC)
class UCAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ano', 'semestre', 'ects', 'licenciatura')
    list_filter = ('ano', 'semestre')
    search_fields = ('nome',)

@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'uc')
    search_fields = ('titulo', 'descricao')

@admin.register(Tecnologia)
class TecnologiaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'nivel_interesse')
    list_filter = ('nivel_interesse',)
    search_fields = ('nome',)

@admin.register(TFC)
class TFCAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autores', 'destaque_interesse')
    list_filter = ('destaque_interesse',)
    search_fields = ('titulo', 'autores')

admin.site.register(Docente)
admin.site.register(Competencia)
admin.site.register(Formacao)