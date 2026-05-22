from django.shortcuts import render, redirect, get_object_or_404
from .models import Licenciatura, UC, Projeto, TFC, Competencia, Tecnologia
from .forms import ProjetoForm, CompetenciaForm, TecnologiaForm
from django.contrib.auth.decorators import user_passes_test

# --- A FECHADURA DE SEGURANÇA ---
# Esta função valida se o utilizador está autenticado e pertence à elite do portfólio
def is_gestor(user):
    return user.is_authenticated and user.groups.filter(name='gestor-portfolio').exists()

# --- PÁGINAS PRINCIPAIS (Abertas ao Público) ---

def index(request):
    return render(request, 'portfolio/index.html')

def academico(request):
    curso = Licenciatura.objects.first()
    ucs = UC.objects.all().order_by('ano', 'semestre')
    tfcs = TFC.objects.all()
    context = {
        'curso': curso,
        'ucs': ucs,
        'tfcs': tfcs,
    }
    return render(request, 'portfolio/academico.html', context)

# --- SECÇÃO CRUD DOS PROJETOS (O teu primeiro motor) ---

def projetos(request):
    lista_projetos = Projeto.objects.all()
    gestor = is_gestor(request.user)
    return render(request, 'portfolio/projetos.html', {'projetos': lista_projetos, 'is_gestor': gestor})

@user_passes_test(is_gestor)
def novo_projeto(request):
    form = ProjetoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('projetos')
    return render(request, 'portfolio/novo_projeto.html', {'form': form})

@user_passes_test(is_gestor)
def editar_projeto(request, projeto_id):
    projeto = get_object_or_404(Projeto, id=projeto_id)
    form = ProjetoForm(request.POST or None, request.FILES or None, instance=projeto)
    if form.is_valid():
        form.save()
        return redirect('projetos')
    return render(request, 'portfolio/novo_projeto.html', {'form': form, 'projeto': projeto})

@user_passes_test(is_gestor)
def apagar_projeto(request, projeto_id):
    projeto = get_object_or_404(Projeto, id=projeto_id)
    if request.method == 'POST':
        projeto.delete()
        return redirect('projetos')
    return render(request, 'portfolio/apagar_projeto.html', {'projeto': projeto})

# --- SECÇÃO CRUD DAS COMPETÊNCIAS (O teu arsenal tático) ---

def competencias(request):
    lista_competencias = Competencia.objects.all()
    lista_tecnologias = Tecnologia.objects.all()
    gestor = is_gestor(request.user)
    context = {
        'competencias': lista_competencias,
        'tecnologias': lista_tecnologias,
        'is_gestor': gestor,
    }
    return render(request, 'portfolio/competencias.html', context)

@user_passes_test(is_gestor)
def nova_competencia(request):
    if request.method == 'POST':
        form = CompetenciaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('competencias')
    else:
        form = CompetenciaForm()
    return render(request, 'portfolio/competencia_form.html', {'form': form, 'acao': 'Nova'})

@user_passes_test(is_gestor)
def editar_competencia(request, competencia_id):
    competencia = get_object_or_404(Competencia, id=competencia_id)
    if request.method == 'POST':
        form = CompetenciaForm(request.POST, instance=competencia)
        if form.is_valid():
            form.save()
            return redirect('competencias')
    else:
        form = CompetenciaForm(instance=competencia)
    return render(request, 'portfolio/competencia_form.html', {'form': form, 'acao': 'Editar'})

@user_passes_test(is_gestor)
def apagar_competencia(request, competencia_id):
    competencia = get_object_or_404(Competencia, id=competencia_id)
    if request.method == 'POST':
        competencia.delete()
        return redirect('competencias')
    return render(request, 'portfolio/apagar_competencia.html', {'competencia': competencia})


# --- SECÇÃO CRUD DAS TECNOLOGIAS (A tua oficina digital) ---

@user_passes_test(is_gestor)
def nova_tecnologia(request):
    form = TecnologiaForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('competencias')
    return render(request, 'portfolio/competencia_form.html', {'form': form, 'acao': 'Nova Tecnologia'})

@user_passes_test(is_gestor)
def editar_tecnologia(request, tecnologia_id):
    tecnologia = get_object_or_404(Tecnologia, id=tecnologia_id)
    form = TecnologiaForm(request.POST or None, request.FILES or None, instance=tecnologia)
    if form.is_valid():
        form.save()
        return redirect('competencias')
    return render(request, 'portfolio/competencia_form.html', {'form': form, 'acao': 'Editar Tecnologia'})

@user_passes_test(is_gestor)
def apagar_tecnologia(request, tecnologia_id):
    tecnologia = get_object_or_404(Tecnologia, id=tecnologia_id)
    if request.method == 'POST':
        tecnologia.delete()
        return redirect('competencias')
    return render(request, 'portfolio/apagar_competencia.html', {'competencia': tecnologia})

# --- OUTRAS PÁGINAS ---

def sobre(request):
    return render(request, 'portfolio/sobre.html')