"""
Aluno:github/kauandragues

Exercício 3: 
Inverter uma string 
Objetivo: Trabalhar com manipulação de strings. 
Descrição: Crie uma função que receba uma string e retorne essa string invertida. 
Dicas: Use slicing (ou fatiamento): texto[::-1] 
"""

def inverter_string(texto:str) -> str:
  return texto[::-1]

texto = input("Digite a sting que deseja inverter:")
print(inverter_string(texto))