"""
Aluno: github/kauandragues

Gerador de Tabuada em Arquivo TXT.
Objetivo: Gerar dados em arquivo a partir de uma estrutura lógica.
Descrição: Crie um arquivo txt e escreva a tabuada de um número informado pelo usuário.
Dicas: Use um loop for de 1 a 10.
"""

num = int(input("Digite um número:"))

with open("tabuada.txt", "w") as arquivo:
  for numero in range(1,11):
    arquivo.write(f"{num} x {numero} = {num*numero}\n")