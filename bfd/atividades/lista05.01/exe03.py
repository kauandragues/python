"""
Aluno: github/kauandragues

Exerício 3:
Gravando Nomes em um Arquivo de Texto.
Objetivo: Aprender a escrever em arquivos de texto.
Descrição: Escreva cinco nomes em um arquivo chamado 'nomes.txt'.
Dicas: Use o modo 'w' com a função open().
"""
nomes = ["Kauã","Rodrigo","Matheus","Giovana","Daniela"]

with open("nomes.txt", "w") as arquivo:
  arquivo.write(", ".join(nomes)) #join junta os nomes, e a string ", " diz para separalos com virgula



