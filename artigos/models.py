from django.db import models
from django.contrib.auth.models import User


class Artigo(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    fotografia = models.ImageField(upload_to='artigos/', blank=True, null=True)
    link_externo = models.URLField(blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='artigos')

    def __str__(self):
        return self.titulo

    def total_likes(self):
        return self.likes.count()


class Like(models.Model):
    artigo = models.ForeignKey(Artigo, on_delete=models.CASCADE, related_name='likes')
    # Qualquer pessoa pode dar like (não precisa de conta)
    # Usamos sessão para controlar — guardamos só o IP como referência
    ip = models.GenericIPAddressField()

    class Meta:
        unique_together = ('artigo', 'ip')

    def __str__(self):
        return f"Like de {self.ip} em '{self.artigo.titulo}'"


class Comentario(models.Model):
    artigo = models.ForeignKey(Artigo, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comentarios')
    texto = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentário de {self.autor.username} em '{self.artigo.titulo}'"