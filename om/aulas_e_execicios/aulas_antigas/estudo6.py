numero = input("Digite um número inteiro:")

try:
    numero = int(numero)
    
    if numero % 2 == 0:
        print(f"O número {numero} é par")
    else:
        print(f"O número {numero} é impar")
except:
    print("O valor não é um número inteiro")