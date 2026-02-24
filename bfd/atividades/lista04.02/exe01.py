"""
Aluno: github/kauandragues

Exercício 1:
Tabuada de um número
Objetivo: Aprofundar o uso de laços de repetição com funções.
Descrição: Crie uma função que receba um número e exiba a tabuada de 1 a 10 para ele.
Dicas: Use um for com range(1, 11) e imprima a multiplicação dentro da função.
"""

def tabuada_numero(num:int):
  for i in range(1,11):
    print(f"{num:2}x{i:2}={num*i:2}")


num = int(input("Digite o número que deseja ver a tabuada:"))
tabuada_numero(num)