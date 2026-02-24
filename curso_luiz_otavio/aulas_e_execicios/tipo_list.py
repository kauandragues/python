listinha = ["kaua",1,4.5,True]
lista1 = [1,2,3,4,5,6]

lista1[2] = 0
del lista1[2] #deleta um item específico

print(lista1)

# print(type(lista), type(listinha))

#se lista é vazio, quando comparada ela dá false

##adicionar coisas no final da lista
lista = [1,2,3,4,5,6]
lista.append(500)
lista.append(600)
lista.pop(0)#retira o último item da lista
lista.insert(0,200)
print(lista)
lista2 = [-1,-2,-3,-4,-5,-6]
print(lista2)
lista3 = lista2 + lista
print(lista3)
lista.extend(lista2)
print(lista)


for item in lista:
    print(item)
