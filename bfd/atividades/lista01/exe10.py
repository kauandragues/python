print("Classificação de idade")
idade = int(input("Digite sua idade: "))
if idade >= 60:
    print(f"Você é idoso e tem {idade} anos")
elif idade >= 18:
    print(f"Você é adulto e tem {idade} anos")
elif idade >= 12:
    print(f"Você é adolescente e tem {idade} anos")
else:
    print(f"Você é criança e tem {idade} anos")