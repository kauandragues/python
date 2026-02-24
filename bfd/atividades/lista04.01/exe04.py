"""
Aluno: github/kauandragues

Exercício 4:
Verificar número par
Objetivo: Trabalhar com condicionais dentro de funções.
Descrição: Crie uma função que receba um número e retorne True se ele for par, False
caso contrário.
Dicas: Use o operador % para verificar o resto da divisão por 2.
"""

def eh_par(num):
  if num % 2 == 0:
    return True
  else:
    return False
  
num = int(input("Digite um inteiro:"))
print(f"É par? {eh_par(num)}")