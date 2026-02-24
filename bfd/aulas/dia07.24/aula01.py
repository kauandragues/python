import csv
conteudo = []
novo_conteudo = []
with open("alunos.csv","r") as arquivo:
  for linha in arquivo:
    conteudo.append(linha.strip().split(","))

for i, linha in enumerate(conteudo):
  for j, elemento in enumerate(linha):
    if int(elemento[1]) >= 7:
      novo_conteudo.append(elemento[0],elemento[1])

print(novo_conteudo) 