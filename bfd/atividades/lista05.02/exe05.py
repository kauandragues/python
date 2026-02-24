"""
Aluno:github/kauandragues

Analisando Estoque com Arquivo CSV
Objetivo: Processar dados de estoque com CSV.
Descrição: Leia um CSV com os campos: produto, preco, quantidade. Calcule o
valor total do estoque.
Dicas: Converta preco e quantidade para numérico, e multiplique para obter o total.
"""
import csv
lista = []

with open("dados_de_estoque.csv","r") as arquivo:
  leitor = csv.reader(arquivo)
  next(leitor)
  lista = list(leitor)

for produto, preco, quantidade in lista:
  print(f"O total de {produto} é R${float(preco)*int(quantidade):.2f}")

