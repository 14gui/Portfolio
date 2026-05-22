from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_artigos, name='lista_artigos'),
    path('novo/', views.criar_artigo, name='criar_artigo'),  # Subiu! Agora o Django apanha-o logo
    path('<int:artigo_id>/', views.detalhe_artigo, name='detalhe_artigo'),
    path('<int:artigo_id>/editar/', views.editar_artigo, name='editar_artigo'),
    path('<int:artigo_id>/apagar/', views.apagar_artigo, name='apagar_artigo'),
    path('<int:artigo_id>/like/', views.dar_like, name='dar_like'),
    path('<int:artigo_id>/comentario/', views.adicionar_comentario, name='adicionar_comentario'),
]