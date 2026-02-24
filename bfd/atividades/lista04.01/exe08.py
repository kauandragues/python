"""
Aluno: github/kauandragues

Exercício 8:
Contar letras de uma palavra
Objetivo: Trabalhar com strings dentro de funções.
Descrição: Crie uma função que receba uma palavra e retorne a quantidade de letras.
Dicas: Use a função len()
"""

def contar_letras(palavra: str):
  return len(palavra)

palavra = input("Digite uma palavra:")
print(f"A palavra {palavra} tem {contar_letras(palavra)} letras")
