nota1 = float(input("Digite a nota1:"))
nota2 = float(input("Digite a nota2:"))
nota3 = float(input("Digite a nota3:"))

def calcular_media(num1, num2, num3):
    return (num1+num2+num3) / 3

print(f"Média: {calcular_media(nota1, nota2, nota3):.2f}")