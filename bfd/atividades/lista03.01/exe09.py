print("Quantas vogais?")
lista_vogais = ["a","e","i","o","u"]
palavra = input("Digite uma palavra:")
qtd_vogais = 0
for letra in palavra:
    for vogal in lista_vogais:
        if letra == vogal:
            qtd_vogais+=1

print(qtd_vogais)
        