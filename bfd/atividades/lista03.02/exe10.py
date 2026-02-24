import random

numero_sorteado = random.randint(1,20)

print("Jogo da Adivinhação!")
while True:
  numero_usuario = int(input("Digite um número:"))
  if numero_usuario == numero_sorteado:
    print("Parabéns! Você acertou!!")
    break;
  elif numero_sorteado > numero_usuario:
    print("Errou! O número sorteado é maior")
  elif numero_sorteado < numero_usuario:
    print("Errou! O número soteado é menor")

  
