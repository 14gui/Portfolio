from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.urls import reverse
from sesame.utils import get_query_string, get_user

# Função para criar conta (Registo)
def view_registo(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/registo.html', {'form': form})

# Função para entrar (Login)
def view_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

# Função para sair (Logout)
def view_logout(request):
    logout(request)
    return redirect('index')

# --- O MOTOR DO MAGIC LINK ---

def pedir_magic_link(request):
    if request.method == 'POST':
        email_inserido = request.POST.get('email')
        try:
            user = User.objects.get(email=email_inserido)
            chave = get_query_string(user, scope="login")
            dominio_real = request.get_host()
            
            # Constrói o link e garante que não tem caracteres problemáticos
            link = f"https://{dominio_real}{reverse('entrar_magic_link')}{chave}"
            
            # Imprime o link limpo diretamente no terminal para copiar
            print("\n" + "="*60)
            print("MAGIC LINK:")
            print(link)
            print("="*60 + "\n")

            send_mail(
                'O teu Acesso Direto ao Portefolio',
                f'Clica aqui: {link}',
                'general@portfolio.com',
                [email_inserido],
                fail_silently=False,
            )
        except User.DoesNotExist:
            pass
        return render(request, 'accounts/email_enviado.html')
    return render(request, 'accounts/pedir_magic.html')

def entrar_magic_link(request):
    user = get_user(request, scope="login")
    if user is not None:
        login(request, user)
        return redirect('index')
    return render(request, 'accounts/erro_magic.html')