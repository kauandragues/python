"""
Aluno: github/kauandragues

Conversão Segura de String para Número.
Objetivo: Praticar conversão de dados e tratamento de exceções.
Descrição: Converta uma string fornecida pelo usuário em número decimal.
Dicas: Use float() dentro de um bloco try.
"""

num = input("Digite um número:")

try:
  float(num)
except ValueError:
  print("Você não digitou um decimal válido")