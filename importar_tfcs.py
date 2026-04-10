import json
import os
import django

# 1. Ligar o script ao teu projeto Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

# 2. Importar o teu modelo TFC
from portfolio.models import TFC

def importar_dados():
    # Caminho para o ficheiro que acabaste de fazer upload
    caminho_ficheiro = 'trabalhos_lusofona.json'
    
    with open(caminho_ficheiro, 'r', encoding='utf-8') as ficheiro:
        dados = json.load(ficheiro)
        
        # 3. Percorrer cada trabalho no JSON e guardar na Base de Dados
        for item in dados:
            TFC.objects.create(
                titulo=item.get('Título', 'Sem Título')[:200],
                autores=item.get('Autor', 'Sem Autor')[:200],
                resumo=item.get('Resumo', ''),
                link_repositorio='https://github.com/Lusofona', # Não existe no JSON, pomos este por defeito
                destaque_interesse=item.get('Raiting', 0) >= 18 # Se teve nota >= 18, fica como destaque!
            )
            
    print(f"Foram importados {len(dados)} trabalhos para a base de dados.")

if __name__ == '__main__':
    importar_dados()