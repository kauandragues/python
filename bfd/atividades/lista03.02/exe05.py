"""
Aluno: github/kauandragues

Sequência de Fibonacci 
Objetivo: Usar for para gerar sequência matemática. 
Descrição: Mostre os 10 primeiros números da sequência de Fibonacci. 
Comece com a = 0, b = 1 e atualize os valores a cada passo 
"""
a = 0
b = 1
auxiliar = 0

for i in range(10):
  print(a)
  auxiliar = b
  b = a + auxiliar
  a = auxiliar
  
