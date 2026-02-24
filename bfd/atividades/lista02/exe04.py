print("IMC")
altura = float(input("Digite sua altura em metros: "))
peso = float(input("Digite o seu peso em kilogramas: "))
imc = peso/altura**2

if imc >= 30:
    print(f"O seu IMC é {imc:.2f} e é classificado como Obeso")
elif imc >= 25:
    print(f"O seu IMC é {imc:.2f} e é classificado como Sobrepeso")
elif imc >= 18.5:
    print(f"O seu IMC é {imc:.2f} e é classificado como Normal")
else:
    print(f"O seu IMC é {imc:.2f} e é classificad como Abaixo do peso")
