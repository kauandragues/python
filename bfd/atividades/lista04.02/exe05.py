"""
Aluno: github/kauandragues

Exercício 5:
Ordenar lista crescente
Objetivo: Usar funções para ordenação de listas.
Descrição: Crie uma função que receba uma lista de números e retorne a lista ordenada em
ordem crescente.
Dicas: Utilize o método .sort() ou a função sorted()
"""

def ordenar_lista(lista:list) -> list:
  return sorted(lista)

lista = [2,2,3,34,5,6,7,3,223,212,664,73,1,2,0,-12]
print(ordenar_lista(lista))


