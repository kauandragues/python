try:
    with open("dados.txt", "r") as arquivo:
        for linha in arquivo:
            print(linha.strip())
except FileNotFoundError:
    print("Erro: o arquivo 'dados.txt' não foi encontado.")

#r - leitura
#w - escrita
#a - acrecentar
#r+ - leitura e escrita