"""
Aluno: github/kauandragues

Exercício 5: 
Dobro de um número 
Objetivo: Realizar cálculos simples com funções. 
Descrição: Crie uma função que receba um número e retorne o dobro do valor. 
Dicas: Multiplique o número por 2 e retorne o resultado. 
"""

def dobrar_num(num):
  return num*2

num = int(input("Digite um número inteiro:"))
print(f"O dobro de {num} é {dobrar_num(num)}")