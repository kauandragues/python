#loops
#for e while
#percorrer sequencias
for item in sequencia:
    #bloco de codigo
    print()

for numero in range (1, 21):
    if numero % 2 ==0:
        print()
        continue

while condicao:
    #bloco de codigo
    break

numero = 1
while numero <=20:
    print()
    numero+=1

#tupla
#imutavel, não muda
#ideal para dados fixos, dias da semana, meses, estados civis
tupla = (1,2,3)

#lista
#mutavel
#ideal para coleções que podem crescer ou mudar
lista = [1,2,3]
lista.append(4)
lista.remove(2)
lista.insert(3,10) #indice e objeto da lista
for item in lista:
    print(item)