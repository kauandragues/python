"""
Aluno: github/kauandragues

Exercício 6: 
Quadrado de um número  
Objetivo: Reforçar operações matemáticas em funções.  
Descrição: Crie uma função que calcule o quadrado de um número.
Dicas: Utilize ** 2 ou n * n. 
"""

def quadrado_num(num):
  return num**2

num = int(input("Digite um número inteiro:"))
print(f"O quadrado de {num} é {quadrado_num(num)}")