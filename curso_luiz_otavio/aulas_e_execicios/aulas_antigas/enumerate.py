#lista unumerada
lista = ["jesus", "maria", "jose"]
lista.append("joao")

lista_enumerada = enumerate(lista)
print(next(lista_enumerada))

#agora eu entendi o desempacotar
for i, item in lista_enumerada:
    print(i, item)