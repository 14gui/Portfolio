from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('academico/', views.academico, name='academico'),
    
    # O teu motor de Projetos
    path('projetos/', views.projetos, name='projetos'),
    path('projetos/novo/', views.novo_projeto, name='novo_projeto'),
    path('projetos/editar/<int:projeto_id>/', views.editar_projeto, name='editar_projeto'),
    path('projetos/apagar/<int:projeto_id>/', views.apagar_projeto, name='apagar_projeto'),
    
    # A tua montra principal de Competências (MANTÉM INTACTA)
    path('competencias/', views.competencias, name='competencias'),
    
    # As três rotas novas de combate para o CRUD das Competências
    path('competencias/nova/', views.nova_competencia, name='nova_competencia'),
    path('competencias/<int:competencia_id>/editar/', views.editar_competencia, name='editar_competencia'),
    path('competencias/<int:competencia_id>/apagar/', views.apagar_competencia, name='apagar_competencia'),

    # As três rotas novas de combate para o CRUD das Tecnologias
    path('tecnologias/nova/', views.nova_tecnologia, name='nova_tecnologia'),
    path('tecnologias/<int:tecnologia_id>/editar/', views.editar_tecnologia, name='editar_tecnologia'),
    path('tecnologias/<int:tecnologia_id>/apagar/', views.apagar_tecnologia, name='apagar_tecnologia'),
    
    path('sobre/', views.sobre, name='sobre'),
    path('artigos/', include('artigos.urls')),

]