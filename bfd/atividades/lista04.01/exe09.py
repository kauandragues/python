"""
Aluno: github/kauandragues

Exercício 9:
Verificar se número é positivo
Objetivo: Usar estrutura condicional em funções.
Descrição: Crie uma função que diga se um número é positivo, negativo ou zero.
Dicas: Use if, elif e else para testar os casos
"""

def jogo_de_sinais(num):
  if num > 0:
    return "positivo"
  elif num == 0:
    return "zero"
  else:
    return "negativo"
  
num = int(input("Digite um número inteiro:"))
print(f"O número {num} é {jogo_de_sinais(num)}")