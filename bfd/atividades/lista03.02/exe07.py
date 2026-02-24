"""
Aluno: github:kauandragues

Multiplicação Cruzada
Objetivo: Trabalhar laços aninhados.
Descrição: Mostre uma tabuada completa de 1 a 5 (ex: 1×1 a 5×10).
Use dois for, um interno e um externo
"""

print("Mostrar tabuadas de 1 a 5")
for numero in range(1,11):
  for tabuada in range (1, 6):
    #end = " | " fala pra o próximo print ser colocado na mesma linha e esse ser separado por |
    print(f"{numero:2d} x{tabuada:2d} = {numero*tabuada:2d}", end=" | ") #o :2d reserva um espaço que será preenchido pela variável
  print()