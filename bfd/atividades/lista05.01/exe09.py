"""
Aluno: github/kauandragues

Exercício 9:
Cadastro de Pessoas em Arquivo CSV.
Objetivo: Criar e manipular arquivos CSV.
Descrição: Escreva nome e idade de 3 pessoas em um arquivo CSV.
Dicas: Use a biblioteca csv e csv.writer
"""
import csv

lista = [["Kauã", 19], ["Pedro", 22], ["Maria", 60]]

with open("arquivo.csv", "w", newline="") as arquivo:
  escritor = csv.writer(arquivo)
  escritor.writerows(lista)
    
  
