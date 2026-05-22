import os
import django
import json

# Ligar o motor do Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from portfolio.models import TFC, Licenciatura

def importar_dados():
    print("A arrombar o cofre dos trabalhos finais...")
    
    # O caminho certo para a pasta data
    caminho_ficheiro = 'data/trabalhos_lusofona.json'
    
    with open(caminho_ficheiro, 'r', encoding='utf-8') as ficheiro:
        dados = json.load(ficheiro)
        
        # Vai buscar a tua licenciatura para associar aos trabalhos
        curso = Licenciatura.objects.first()
        
        for item in dados:
            TFC.objects.create(
                titulo=item['titulo'],
                autores=item['autores'],
                resumo=item['resumo'],
                link_repositorio=item['link_repositorio'],
                licenciatura=curso
            )
            
    print("Trabalhos importados com sucesso absoluto!")

if __name__ == '__main__':
    importar_dados()