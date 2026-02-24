"""
split e join e strip
"""

frase = "Olha só que, coisa interessante"
lista_palavras = frase.split(sep=",")
lista = ["1","2"]

for i, frase in enumerate(lista_palavras):
    lista[i] = lista_palavras[i].strip() #rstrip() é tirar o espaço da direita e lstrip() é o da esquerda

for i, frase in enumerate(lista_palavras):
    print(lista[i])

frases_unidas = "".join(lista_palavras)
print(frases_unidas)