"""
Aluno: github/kauandragues

Exercício 10:
Filtrando Pessoas por Idade no CSV.
Objetivo: Filtrar dados de um arquivo CSV.
Descrição: Leia o CSV do exercício anterior e exiba apenas pessoas com idade maior que 20.
Dicas: Converta a idade para inteiro e use um if
"""
import csv
conteudo = []

with open("arquivo.csv", "r", newline="") as arquivo:
  lido = csv.reader(arquivo)
  conteudo = list(lido)

for nome, idade in conteudo:
  if int(idade) > 20:
    print(f"{nome} tem {idade}")
