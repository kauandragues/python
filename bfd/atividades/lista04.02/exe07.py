"""
Aluno: github/kauandragues

Converter número para binário
Objetivo: Trabalhar com conversão de base numérica.
Descrição: Crie uma função que receba um número inteiro e retorne sua representação em
binário.
Dicas: Use a função bin(numero) e remova o prefixo '0b' com slicing
"""
def transforma_int_binario(num:int) -> str:
  return bin(num)[2::]

num = int(input("Digite um número inteiro:"))
print(transforma_int_binario(num))
