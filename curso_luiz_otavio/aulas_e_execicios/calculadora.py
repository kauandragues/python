while True:
    print("Menu")
    print("0 -> Soma")
    print("1 -> Subtração")
    print("2 -> Multiplicação")
    print("3 -> Divisão")
    print("4 -> Sair")
    try:
        opcao = int(input("\nDigite uma das opções:"))
    except ValueError:
        print("Você não digitou um dos inteiros!!")
        continue

    if opcao == 0:

        print("\nSomando!")

        numero1 = int(input("Digite o primeiro número:"))
        numero2 = int(input("Digite o segundo número:"))
        resultado = numero1 + numero2
        print(f"Reultado de {numero1} + {numero2} = {resultado}\n")

    elif opcao == 1:

        print("\nSubtraindo!")
        numero1 = int(input("Digite o primeiro número:"))
        numero2 = int(input("Digite o segundo número:"))
        resultado = numero1 - numero2
        print(f"Reultado de {numero1} - {numero2} = {resultado}\n")

    elif opcao == 2:

        print("\nMultiplicando!")
        numero1 = int(input("Digite o primeiro número:"))
        numero2 = int(input("Digite o segundo número:"))
        resultado = numero1 * numero2
        print(f"Reultado de {numero1} * {numero2} = {resultado}\n")

    elif opcao == 3:

        print("\nDividindo!")
        numero1 = int(input("Digite o primeiro número:"))
        numero2 = int(input("Digite o segundo número:"))
        resultado = numero1 / numero2
        print(f"Reultado de {numero1} / {numero2} = {resultado}\n")

    elif opcao == 4:

        print("\nSaindo do programa...")
        break

    else:

        print("Digite uma opção válida!")
