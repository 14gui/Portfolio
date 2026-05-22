import os
import django
import requests

# Ligar o motor do Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from portfolio.models import UC, Licenciatura

def importar_ucs():
    print("A invadir a API secreta da Lusófona...")
    
    # ATENÇÃO Mete aqui o teu link verdadeiro da API!
    url = "COLOCA AQUI O TEU LINK" 
    
    resposta = requests.get(url)
    dados = resposta.json()
    
    curso = Licenciatura.objects.first()
    
    for uc in dados:
        UC.objects.create(
            nome=uc['nome'],
            ano=uc['ano'],
            # A MÁGICA ESTÁ AQUI O Python corta a string e guarda só o número!
            semestre=int(str(uc['semestre'])[0]), 
            ects=uc['ects'],
            licenciatura=curso
        )
        
    print("Cadeiras importadas para a base de dados!")

if __name__ == '__main__':
    importar_ucs()