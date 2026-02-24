"""
Aluno: github/kauandragues

Exercício 2: 
Quadrado dos elementos de uma lista  
Objetivo: Manipular listas com funções e realizar operações sobre seus elementos. 
Descrição: Crie uma função que receba uma lista e retorne outra lista com os elementos elevados ao quadrado.  
Dicas: Use laço for e operador ** para o cálculo. 
"""
lista = []
def lista_ao_quadrado(lista:list) -> list: #esse seta diz o que será retornado :)
  lista_quadrada = []
  for elemento in lista:
    lista_quadrada.append(elemento*elemento)
  
  return lista_quadrada

qtd_elementos_lista = int(input("Digite a quantidade de elemento da lista:"))
for elemento in range(qtd_elementos_lista):
  lista.append(int(input("Digite o elemento que será adicionado na lista:")))

print(lista)
lista = lista_ao_quadrado(lista)
print(lista)

