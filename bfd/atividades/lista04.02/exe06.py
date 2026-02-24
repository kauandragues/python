"""
Aluno: github/kauandragues

Formatar uma data
Objetivo: Trabalhar com parâmetros múltiplos e formatação de strings.
Descrição: Crie uma função que receba dia, mês e ano e retorne a data no formato
dd/mm/aaaa.
Dicas: Use f-strings ou concatenação para formatar.
"""

def formatar_data(dia:int, mes:int, ano:int) -> str:
  return f"{dia:0{2}}/{mes:0{2}}/{ano:0{4}}" #formatando para ficar 00/00/0000

dia = int(input("Digite o dia:"))
mes = int(input("Digite o mês:"))
ano = int(input("Digite o ano:"))

print(formatar_data(dia, mes, ano))
