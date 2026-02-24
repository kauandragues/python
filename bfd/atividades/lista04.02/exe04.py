"""
Aluno:github/kauandragues

Filtrar números pares de uma lista
Objetivo: Utilizar estruturas condicionais com listas dentro de funções.
Descrição: Crie uma função que receba uma lista de números e retorne somente os pares.
Dicas: Use uma lista auxiliar ou list comprehension com if n % 2 == 0

"""
lista = [1,2,3,4,5,6,7,8,9,10]
def lista_pares(lista:list) -> list:
  return [num for num in lista if num % 2 == 0]

print(lista_pares(lista))