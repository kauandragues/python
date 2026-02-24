"""
Aluno: github/kauandragues

Exercício 9: 
Verificar se é múltiplo de 3 e 5 
Objetivo: Aplicar lógica booleana e divisibilidade em funções. 
Descrição: Crie uma função que diga se um número é múltiplo de 3 e de 5 ao mesmo tempo. 
Dicas: Use operadores %, and e if. 
"""

def verificar_se_multiplo_3_e_5(num:int) -> str:
  if(num % 3 == 0 and num % 5 == 0):
    return "SIM"
  return "NÃO"

num = int(input("Digite um número:"))
print(f"É múltiplo de 3 e 5? {verificar_se_multiplo_3_e_5(num)}")