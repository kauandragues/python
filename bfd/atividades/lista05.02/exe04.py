"""
Aluno: github/kauandragues

Calculadora com Tratamento de Erros
Objetivo: Criar uma calculadora robusta.
Descrição: Faça uma calculadora que trate erros como entrada inválida, operação inválida e
divisão por zero.
Dicas: Use try/except para capturar ValueError e ZeroDivisionError, valide a
operação com if.
"""

def somar_numeros(a,b):
  return a+b

def dividir_numeros(a,b):
  try:
    return a/b
  except ZeroDivisionError:
    print("\nVocê tentou dividir por 0, operação inválida!")

def subtrair_numeros(a,b):
   return a-b

def multiplicar_numeros(a,b):
  return a*b

def ler_um_numero():
  try:
    a = int(input("Digite um inteiro:"))
    return a
  except ValueError:
    print("Você não digitou um inteiro")

#menu
#execução principal
print("Calculadora!\n")
print("Digite uma opção:\n")
print("1-Somar\n")
print("2-Subtrair\n")
print("3-Dividir\n")
print("4-Multiplicar\n")

#validação da opção
try:
  opcao = int(input("Digite o número da opção:"))
except ValueError:
  print("Você não digitou um número!")
if opcao not in [1,2,3,4]:
  print("Você digitou uma opção inválida\n")
elif opcao == 1:
  a = ler_um_numero()
  b = ler_um_numero()
  resultado = somar_numeros(a,b)
elif opcao == 2:
  a = ler_um_numero()
  b = ler_um_numero()
  resultado = subtrair_numeros(a,b)
elif opcao == 3:
  a = ler_um_numero()
  b = ler_um_numero()
  resultado = dividir_numeros(a,b)
elif opcao == 4:
  a = ler_um_numero()
  b = ler_um_numero()
  resultado = multiplicar_numeros(a,b)

print(f"\nO resultado da sua operação foi {resultado}")


