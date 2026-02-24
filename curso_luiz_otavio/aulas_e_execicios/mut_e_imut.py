variavel1 = [20]
variavel2 = variavel1 #não é criada outra lista, mas sim, a variavel2 aponta para a lista da variavel1
#isso acontece pq a list é um tipo mutável
variavel1[0] = 30

variavel2 = variavel1.copy() #assim é como se copia os valores e cria uma lista nova
print(variavel2)