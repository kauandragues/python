num1 = input("Digite um valor:")
num2 = input("Digite outro valor:")

if(num1 > num2):
    print(f"{num1=} é maior que {num2=}")
elif(num2 > num1):
    print(f"{num2=} é maior que {num1=}")
else:
    print(f"{num1=} e {num2=} são iguais")