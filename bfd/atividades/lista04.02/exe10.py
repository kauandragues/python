"""
Aluno: github/kauandragues

Exercício 10:
Jogo de adivinhação 
Objetivo: Usar bibliotecas externas, entrada de dados e lógica condicional. 
Descrição: Crie uma função que sorteie um número entre 1 e 10 e peça que o usuário tente 
adivinhar. 
Dicas: Use import random, input() e if para comparar os valores 
"""
import random

def sortear_numero_de_1_a_10() -> int:

  return random.randint(40,52)

def checar_se_acertou_ou_errou(numero_sorteado:int, numero_escolhido:int) -> bool:

  if(numero_sorteado == numero_escolhido):
    return True
  
  return False

numero_sorteado = sortear_numero_de_1_a_10()
while True:
  numero_escolhido = int(input("Tente adivinhar o número:"))

  if(checar_se_acertou_ou_errou(numero_sorteado,numero_escolhido)):
    print("Acertou o número!!")
    break
  
  print("Errou o número, tente novamento!\n")
  






