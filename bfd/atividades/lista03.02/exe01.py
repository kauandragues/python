lista_impares = []
lista_pares = []

print("Criação de uma lista de pares e impares")
qtd_inteiros = int(input("Digite a quantidade de inteiros:"))

for inteiro in range(qtd_inteiros):
    numero_atual = int(input("Digite um inteiro: "))
    if numero_atual % 2 != 0: #se for impar coloque na lista dos impares
        lista_impares.append(numero_atual)
    else:
        lista_pares.append(numero_atual)

#mostrar listas
print("Os números pares são")
for pares in lista_pares:
    print(pares)

print("Os números impares são")
for impares in lista_impares:
    print(impares)
