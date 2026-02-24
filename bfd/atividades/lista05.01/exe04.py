"""
Aluno: github/kauandragues

Exerício 4: 
Leitura Linha a Linha de Arquivo de Texto. 
Objetivo: Praticar leitura de arquivos linha a linha 
Descrição: Leia o conteúdo de 'nomes.txt' e exiba cada linha separadamente. 
Dicas: Use um loop for para iterar sobre o arquivo. 
"""
conteudo = []

with open("nomes.txt", "r") as arquivo:
    for linha in arquivo:
        conteudo.append(linha.strip())

for linha in conteudo:
    print(linha)

