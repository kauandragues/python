"""
Aluno: github/kauandragues

Objetivo: Filtrar valores únicos em uma lista. 
Descrição: Dada uma lista com repetições, crie uma nova sem duplicatas. 
Use not in ou set()
"""

lista_com_duplicadas = [1,2,3,4,5,5,5,5,6,7,3,3,4,]
lista_sem_duplicadas = []

for item in lista_com_duplicadas:
  if item not in lista_sem_duplicadas:
    lista_sem_duplicadas.append(item)

print(lista_sem_duplicadas)    