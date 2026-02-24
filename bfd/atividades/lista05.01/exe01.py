"""
Aluno: Kauã de Andrade Rodrigues

Entrada Segura de Números.
Objetivo: Praticar entrada de dados e tratamento de exceções.
Descrição: Peça ao usuário um número inteiro. Se ele digitar um texto, informe o erro de
forma amigável.
Dicas: Use try/except com a função int().
"""
try:
  num = int(input("Digite um número inteiro: "))
except:
  print("Você digitou um texto, digite apenas o número inteiro!!")