from django.db import models

class Licenciatura(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    ano_inicio = models.IntegerField()

    def __str__(self):
        return self.nome

class Docente(models.Model):
    nome = models.CharField(max_length=100)
    link_lusofona = models.URLField()

    def __str__(self):
        return self.nome

class UC(models.Model):
    nome = models.CharField(max_length=100)
    ano = models.IntegerField()
    semestre = models.IntegerField()
    ects = models.IntegerField()
    imagem = models.ImageField(upload_to='ucs/', blank=True, null=True)
    
    # Relações que desenhaste no papel:
    licenciatura = models.ForeignKey(Licenciatura, on_delete=models.CASCADE, related_name='ucs')
    docentes = models.ManyToManyField(Docente, related_name='ucs')

    def __str__(self):
        return self.nome

class Projeto(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    conceitos_aplicados = models.TextField()
    imagem = models.ImageField(upload_to='projetos/', blank=True, null=True)
    video_demo = models.URLField(blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)
    
    # Relação: 1 UC tem vários Projetos
    uc = models.ForeignKey(UC, on_delete=models.CASCADE, related_name='projetos')

    def __str__(self):
        return self.titulo

class Tecnologia(models.Model):
    nome = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='tecnologias/', blank=True, null=True)
    link_oficial = models.URLField()
    nivel_interesse = models.IntegerField() # Ex: 1 a 5
    descricao_destaque = models.TextField()
    
    # Relação: Tecnologias usadas em Projetos
    projetos = models.ManyToManyField(Projeto, related_name='tecnologias')

    def __str__(self):
        return self.nome

class Competencia(models.Model):
    nome = models.CharField(max_length=50)
    nivel = models.CharField(max_length=50) # Ex: Iniciante, Intermédio, Avançado
    categoria = models.CharField(max_length=50) # Ex: Hard Skill, Soft Skill
    
    # Relação: Competências demonstradas em Projetos
    projetos = models.ManyToManyField(Projeto, related_name='competencias')

    def __str__(self):
        return self.nome

class Formacao(models.Model):
    titulo_curso = models.CharField(max_length=100)
    instituicao = models.CharField(max_length=100)
    data_inicio = models.DateField()
    data_fim = models.DateField(blank=True, null=True)
    
    # NOVA RELAÇÃO: Formações exigem Competências (N para N)
    competencias = models.ManyToManyField(Competencia, related_name='formacoes')

    def __str__(self):
        return f"{self.titulo_curso} ({self.instituicao})"

class TFC(models.Model):
    titulo = models.CharField(max_length=200)
    autores = models.CharField(max_length=200)
    resumo = models.TextField()
    link_repositorio = models.URLField()
    destaque_interesse = models.BooleanField(default=False)
    
    # NOVA RELAÇÃO: TFC pertence a Licenciatura (N para 1)
    licenciatura = models.ForeignKey(Licenciatura, on_delete=models.CASCADE, related_name='tfcs', null=True)

    def __str__(self):
        return self.titulo
