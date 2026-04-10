# Portfólio Universitário - Parte 1 (Backend)

Este repositório contém o código da primeira fase do meu Portfólio Universitário desenvolvido em Django. Esta etapa focou-se na modelação da base de dados, configuração do painel de administração e criação de scripts para importação automática de dados.

---

## 1. Modelação da Base de Dados

O trabalho começou pelo desenho da arquitetura da base de dados. O diagrama abaixo mostra como as entidades principais (Licenciaturas, UCs, Projetos, Competências, Tecnologias e Docentes) se relacionam.

A nível de estrutura, optei por criar relações de N:M (muitos para muitos) entre Projetos e Tecnologias para garantir maior flexibilidade na associação de várias ferramentas a um único projeto, e uma relação de 1:N (um para muitos) entre a Licenciatura e os Trabalhos Finais de Curso (TFCs). Como valor acrescentado ao modelo base, foi introduzida a entidade **Docente**, permitindo associar os professores às respetivas Unidades Curriculares ou trabalhos orientados, enriquecendo assim a informação disponível no portfólio.

![Diagrama de Entidade-Relação](media/makingof/Modelo%20Entidade%201.jpg)

## 2. Painel de Administração Django

O backoffice nativo do Django (`/admin`) foi adaptado para facilitar a gestão dos conteúdos do portfólio:
* Foram aplicados filtros de pesquisa por ano e semestre nas UCs, e por nível de interesse nas Tecnologias.
* Foram incluídas barras de pesquisa nas tabelas com maior volume de dados (Licenciaturas, Projetos e TFCs) para acelerar a localização de registos.
* As listas de visualização (`list_display`) foram configuradas em todos os modelos para apresentar apenas os atributos mais relevantes, tornando a interface mais limpa.

## 3. Scripts de Importação de Dados

Para evitar a inserção manual e morosa de dados no backoffice, foram desenvolvidos scripts em Python para preencher a base de dados de forma automática:

* **Importação de TFCs (`importar_tfcs.py`):** O script processa um ficheiro JSON local com os dados dos Trabalhos Finais de Curso e insere-os diretamente na tabela `TFC` da base de dados. Foi implementada uma lógica de validação onde os TFCs com nota igual ou superior a 18 recebem a flag de destaque automaticamente.
* **Integração com a API da Lusófona (`importar_ucs.py`):** Em vez de gerar ficheiros de texto intermédios, este script faz pedidos HTTP diretamente à API pública da universidade. O script recolhe o plano de estudos do curso de Engenharia Informática, processa a resposta em formato JSON e regista as UCs na base de dados, estabelecendo logo a relação com a licenciatura respetiva.

---
**Nota:** Projeto desenvolvido no âmbito da disciplina de Web.