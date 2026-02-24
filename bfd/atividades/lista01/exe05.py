print("Calcular média e mostrar aprovação")
nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite a sua segunda nota: "))
media = (nota1 + nota2) / 2

if media >= 6:
    print(f"Você foi aprovado com {media} de média")
else:
    print(f"Você foi reprovado com {media} de média")