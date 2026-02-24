"""
Aluno: github/kauandragues

Números Primos
Objetivo: Verificar condição especial em loop.
Descrição: Mostre todos os números primos entre 1 e 50.
🧠 Dica: Um número é primo se for divisível apenas por 1 e ele mesmo
"""
for numero in range(2, 51):
  #irá percorrer todos os números anteriores até o número atual
  eh_primo = 1 #variavel para testar depois se algum número foi divisivel pelo número atual
  for antecessores in range(2, numero):
    #se for divisivel por qualquer um deles, significa que é primo e não precisa continuar
    if numero % antecessores == 0:
      eh_primo = 0
      break;
  
  if eh_primo == 1:
    print(numero)