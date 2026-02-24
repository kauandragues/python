"""
Aluno: github/kauandragues

Exercício 5:
Divisão com Tratamento de Erros.
Objetivo: Tratar divisão por zero.
Descrição: Peça dois números ao usuário e realize a divisão, tratando divisão por zero.
Dicas: Use try/except para capturar ZeroDivisionError.
"""

num1 = int(input("Digite um número:"))
num2 = int(input("Digite outro número:"))

try:
  divisao = num1 / num2
except ZeroDivisionError:
  print("Você tentou dividir por 0, tente novamente")