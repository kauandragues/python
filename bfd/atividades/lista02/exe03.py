print("Calculo de média e aprovação")
nota1 = float(input("Digite a primeira nota: "))
peso1 = float(input("Digite o peso da primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
peso2 = float(input("Digite o peso da segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
peso3 = float(input("Digite o peso da terceira nota: "))

media = ((nota1*peso1)+(nota2*peso2)+(nota3*peso3)) / (peso1+peso2+peso3)
if media >= 6:
    print(f"Você foi aprovado com {media} de média")
else:
    print(f"Você foi reprovado com {media} de média")