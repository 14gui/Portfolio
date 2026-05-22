import os
import django

# Garante que o Django está carregado antes de falar com a base de dados
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from django.core.files import File
from portfolio.models import UC, Projeto, Tecnologia

print("A iniciar migração de imagens para o Cloudinary...")

# 1. Migrar imagens das UCs
for uc in UC.objects.all():
    if uc.imagem and uc.imagem.name and os.path.exists(uc.imagem.path):
        print(f"A enviar imagem da UC: '{uc.nome}'...")
        with open(uc.imagem.path, 'rb') as f:
            uc.imagem.save(os.path.basename(uc.imagem.path), File(f), save=True)

# 2. Migrar imagens dos Projetos
for proj in Projeto.objects.all():
    if proj.imagem and proj.imagem.name and os.path.exists(proj.imagem.path):
        print(f"A enviar imagem do Projeto: '{proj.titulo}'...")
        with open(proj.imagem.path, 'rb') as f:
            proj.imagem.save(os.path.basename(proj.imagem.path), File(f), save=True)

# 3. Migrar logos das Tecnologias
for tec in Tecnologia.objects.all():
    if tec.logo and tec.logo.name and os.path.exists(tec.logo.path):
        print(f"A enviar logo da Tecnologia: '{tec.nome}'...")
        with open(tec.logo.path, 'rb') as f:
            tec.logo.save(os.path.basename(tec.logo.path), File(f), save=True)

print("Migração concluída com sucesso no Cloudinary!")