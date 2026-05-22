from django import forms
from .models import Artigo, Comentario


class ArtigoForm(forms.ModelForm):
    class Meta:
        model = Artigo
        # Voltamos a usar 'link_externo' para bater certo com o teu models.py!
        fields = ['titulo', 'texto', 'fotografia', 'link_externo']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título do artigo'}),
            'texto': forms.Textarea(attrs={'class': 'form-control', 'rows': 8, 'placeholder': 'Escreve o teu artigo...'}),
            'fotografia': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'link_externo': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://...'}),
        }


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto']
        widgets = {
            'texto': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Escreve o teu comentário...'
            }),
        }
        labels = {
            'texto': '',
        }

