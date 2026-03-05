import os
lista_de_compras = []

while True:

    print("lista de compras\n" \
    "(i)nserir | (a)pagar | (l)istar")
    opcao = input("Digite umas das opção:").lower()

    match opcao:

        case "i":
            os.system("clear")
            item = input("Digite o item que deseja inserir:")
            lista_de_compras.append(item)   

        case "a":
            os.system("clear")
            indice_do_item = int(input("Digite o índice do item que deseja apagar"))

            if 0 <= indice_do_item < len(lista_de_compras):
                lista_de_compras.pop(indice_do_item)

            else:
                print("esse índice não existe")

        case "l":
            os.system("clear")
            if len(lista_de_compras) != 0:
                print("mostrando a lista de compras:")
                for i, item in enumerate(lista_de_compras):
                    print(i, item)

            else:
                print("O lista está vazia")

        case _:
            os.system("clear")
            print("opção inválida")
