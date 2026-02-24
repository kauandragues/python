"""
Aluno: github/kauandragues

Substituindo Palavras em Arquivo TXT
Objetivo: Editar o conteúdo de arquivos txt.
Descrição: Escreva um programa que substitui uma palavra por outra dentro de um arquivo
.txt.
Dicas: Leia todo o conteúdo com .read(), use .replace(), e escreva de volta no
arquivo.
"""
conteudo = ""

with open("arquivos.txt", "r") as arquivo:
  leitor = arquivo.read()
  conteudo = leitor

conteudo = conteudo.replace("bem", "ótimo")

with open("arquivos.txt", "w") as arquivo:
  arquivo.write(conteudo)
