"""
Aluno: github/kauandragues

Catálogo de Livros em CSV com Busca
Objetivo: Manipular estrutura de dados com arquivos.
Descrição: Crie um arquivo CSV com dados de 5 livros (título, autor, ano) e implemente
uma busca por título.
Dicas: Use csv.DictWriter e depois csv.DictReader para ler e fazer comparações
com if.
"""
import csv
livros = []
busca = input("Digite o título do livro:")

with open("livros.csv","r",newline="") as arquivo_livro:
  leitor = csv.reader(arquivo_livro)
  next(leitor)
  livros = list(leitor)

for livro, autor, ano in livros:
  if livro.lower() == busca.lower():
    print("O livro que você procura é:\n")
    print(f"{livro} escrito por {autor} e publicado em {ano}")

