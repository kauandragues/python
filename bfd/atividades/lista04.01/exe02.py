"""
Aluno: github/kauandragues

Exercício 2: 
Saudação com nome 
Objetivo: Utilizar parâmetros em funções. 
Descrição: Crie uma função chamada saudacao que receba um nome e exiba 'Olá, [nome]!' 
Dicas: Lembre-se de usar um parâmetro e concatenar ou formatar a string. 
"""

def saudacao(nome: str):
  print(f"Olá! {nome}")

nome = input("Digite um nome:")
saudacao(nome)