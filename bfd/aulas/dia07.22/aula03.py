import csv
with open("alunos.csv","w",newline="") as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerow(["Nome", "Nota"])
    escritor.writerow(["Ana", 8.5])
    escritor.writerow(["Carlos", 6.7])

with open("alunos.csv","r") as arquivo:
    leitor = csv.reader(arquivo)
    for linha in leitor:
        print(linha)