"""
Aluno: github/kauandragues

Exercício 1:
Contador de Linhas de Arquivo TXT
Objetivo: Contar linhas de um arquivo.
Descrição: Leia um arquivo .txt e mostre quantas linhas ele possui.
Dicas: Use a função readlines() ou itere com for e enumerate() para contar.
"""

numero_linhas = 0

with open("numero_linhas.txt","r") as arquivo:
  for linha in arquivo:
    numero_linhas += 1

print(f"O arquivo tem {numero_linhas} linhas")
