"""
Aluno: github/kauandragues

Exercício 8: 
Área de um retângulo 
Objetivo: Criar funções para cálculos geométricos. 
Descrição: Crie uma função que receba base e altura e retorne a área de um retângulo. 
Dicas: Multiplique base por altura e retorne o valor. 
"""

def calcular_area_retangulo(base:float, altura:float) -> float:
  return base*altura

base = float(input("Digite a base do retângulo:"))
altura = float(input("Digite a altura do retângulo:"))

print(calcular_area_retangulo(base, altura))