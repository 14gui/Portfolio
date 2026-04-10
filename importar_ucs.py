import os
import django
import requests

# 1. Ligar o script ao teu projeto Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from portfolio.models import UC, Licenciatura

def importar_ucs():
    print("A aceder à API secreta da Lusófona...")
    
    # URL e dados retirados da tua ficha para o curso de LEI (260)
    url = 'https://secure.ensinolusofona.pt/dados-publicos-academicos/resources/GetCourseDetail'
    payload = {
        'language': 'PT',
        'courseCode': 260, # Código de Eng. Informática
        'schoolYear': '202425'
    }
    headers = {'content-type': 'application/json'}
    
    resposta = requests.post(url, json=payload, headers=headers)
    
    if resposta.status_code == 200:
        dados = resposta.json()
        plano_estudos = dados.get('courseFlatPlan', [])
        
        # Vai buscar a tua Licenciatura para associar às UCs
        licenciatura = Licenciatura.objects.first()
        contador = 0
        
        for uc in plano_estudos:
            # Vai buscar os dados específicos de cada disciplina
            nome = uc.get('curricularUnitName', 'Sem Nome')
            ano = uc.get('curricularYear', 1)
            semestre = uc.get('semester', 1)
            ects = uc.get('ects', 6)
            
            # Guarda na base de dados
            UC.objects.create(
                nome=nome,
                ano=ano,
                semestre=semestre,
                ects=ects,
                licenciatura=licenciatura
            )
            contador += 1
            
        print(f"Foram importadas {contador} UCs para a base de dados.")
    else:
        print(f"Erro ao aceder à API. Código: {resposta.status_code}")

if __name__ == '__main__':
    importar_ucs()