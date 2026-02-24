import random
numero_sorteiado = random.randint(1,10)
tentativas = 1
while True:
    numero_usuario = int(input("Digite um número:"))
    if numero_usuario == numero_sorteiado:
        print(f"Parabéns! Você acertou em {tentativas} tentativas")
        break
    elif numero_usuario < numero_sorteiado:
        print(F"Errou! O número sorteado é maior!! Você está na tentativa {tentativas}")
        tentativas+=1
    else:
        print(f"Errou! O número sorteado é menor!! Você está na tentativa {tentativas}")
        tentativas+=1
