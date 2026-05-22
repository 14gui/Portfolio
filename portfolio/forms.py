from django import forms
from .models import Projeto, Competencia, Tecnologia

class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = '__all__'

class CompetenciaForm(forms.ModelForm):
    class Meta:
        model = Competencia
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Python ou Trabalho em Equipa'}),
            'nivel': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Iniciante, Intermédio, Avançado'}),
            'categoria': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Hard Skill ou Soft Skill'}),
        }

class TecnologiaForm(forms.ModelForm):
    class Meta:
        model = Tecnologia
        fields = '__all__'