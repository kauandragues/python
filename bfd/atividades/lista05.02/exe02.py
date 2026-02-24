"""
Aluno: github/kauandragues

Calculando Médias com Arquivo CSV
Objetivo: Trabalhar com leitura e escrita em CSV.
Descrição: Leia notas de alunos a partir de um arquivo CSV e gere outro arquivo com a
média de cada aluno.
"""
import csv

alunos = []

with open("notas.csv","r") as arquivo_notas:
  leitor = csv.reader(arquivo_notas)
  next(leitor) #pular o cabeçalho
  alunos = list(leitor)

with open("medias_alunos.csv","w",newline="") as arquivo_medias:
  escritor = csv.writer(arquivo_medias)
  escritor.writerow(["Nome","Média"])

  for nome, nota1, nota2, nota3 in alunos:
    escritor.writerow([nome,round((float(nota1)+float(nota2)+float(nota3))/3,2)])