from django.urls import path
from . import views

urlpatterns = [
    path('registo/', views.view_registo, name='registo'),
    path('login/', views.view_login, name='login'),
    path('logout/', views.view_logout, name='logout'),

    # As estradas novas do Magic Link
    path('entrar-magico/', views.pedir_magic_link, name='pedir_magic_link'),
    path('autenticar/', views.entrar_magic_link, name='entrar_magic_link'),
]