print("Média de 4 notas")
lista_notas = []
soma = 0
media = 0
for i in range(4):
    lista_notas.append(float(input("Digite a nota:")))
    soma = soma + lista_notas[i]

media = soma / 4
if media >= 6:
    print(f"Parabéns! Você foi aprovado com {media} de média")
else:
    print(f"Que pena! Você foi reprovado com {media} de média")

