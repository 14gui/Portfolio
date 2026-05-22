from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Artigo, Like, Comentario
from .forms import ArtigoForm, ComentarioForm


def lista_artigos(request):
    artigos = Artigo.objects.all().order_by('-data_criacao')
    # CORREÇÃO: Mudado de 'articles' para 'artigos' para evitar NameError
    return render(request, 'artigos/lista.html', {'artigos': artigos})


def detalhe_artigo(request, artigo_id):
    artigo = get_object_or_404(Artigo, id=artigo_id)
    comentarios = artigo.comentarios.all().order_by('-data_criacao')
    form_comentario = ComentarioForm()

    # Verifica se o utilizador já deu like (pelo IP)
    ip = request.META.get('REMOTE_ADDR')
    ja_deu_like = artigo.likes.filter(ip=ip).exists()

    return render(request, 'artigos/detalhe.html', {
        'artigo': artigo,
        'comentarios': comentarios,
        'form_comentario': form_comentario,
        'ja_deu_like': ja_deu_like,
    })


@login_required
def criar_artigo(request):
    # Só autores podem criar
    if not request.user.groups.filter(name='autores').exists():
        messages.error(request, 'Não tens permissão para publicar artigos.')
        return redirect('lista_artigos')

    if request.method == 'POST':
        form = ArtigoForm(request.POST, request.FILES)
        if form.is_valid():
            artigo = form.save(commit=False)
            artigo.autor = request.user
            artigo.save()
            messages.success(request, 'Artigo publicado com sucesso!')
            return redirect('detalhe_artigo', artigo_id=artigo.id)
    else:
        form = ArtigoForm()

    # CORREÇÃO: Aponta para 'form_artigo.html' que é o teu ficheiro real no VS Code
    return render(request, 'artigos/form_artigo.html', {'form': form, 'titulo': 'Novo Artigo'})


@login_required
def editar_artigo(request, artigo_id):
    artigo = get_object_or_404(Artigo, id=artigo_id)

    # Só o próprio autor pode editar
    if artigo.autor != request.user:
        messages.error(request, 'Só podes editar os teus próprios artigos.')
        return redirect('detalhe_artigo', artigo_id=artigo.id)

    if request.method == 'POST':
        form = ArtigoForm(request.POST, request.FILES, instance=artigo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Artigo atualizado!')
            return redirect('detalhe_artigo', artigo_id=artigo.id)
    else:
        form = ArtigoForm(instance=artigo)

    # CORREÇÃO: Aponta para 'form_artigo.html' que é o teu ficheiro real no VS Code
    return render(request, 'artigos/form_artigo.html', {'form': form, 'titulo': 'Editar Artigo'})


@login_required
def apagar_artigo(request, artigo_id):
    artigo = get_object_or_404(Artigo, id=artigo_id)

    if artigo.autor != request.user:
        messages.error(request, 'Só podes apagar os teus próprios artigos.')
        return redirect('detalhe_artigo', artigo_id=artigo.id)

    if request.method == 'POST':
        artigo.delete()
        messages.success(request, 'Artigo apagado.')
        return redirect('lista_artigos')

    return render(request, 'artigos/confirmar_apagar.html', {'artigo': artigo})


def dar_like(request, artigo_id):
    artigo = get_object_or_404(Artigo, id=artigo_id)
    ip = request.META.get('REMOTE_ADDR')

    like_existente = artigo.likes.filter(ip=ip).first()
    if like_existente:
        like_existente.delete()  # Toggle: remove o like se já existir
    else:
        Like.objects.create(artigo=artigo, ip=ip)

    return redirect('detalhe_artigo', artigo_id=artigo.id)


@login_required
def adicionar_comentario(request, artigo_id):
    artigo = get_object_or_404(Artigo, id=artigo_id)

    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.artigo = artigo
            comentario.autor = request.user
            comentario.save()

    return redirect('detalhe_artigo', artigo_id=artigo.id)