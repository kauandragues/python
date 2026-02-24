"""
Aluno:github/kauandragues

Exercício 10:
Contador de Palavras em Arquivo
Objetivo: Analisar conteúdo textual.
Descrição: Solicite o nome de um arquivo .txt ao usuário e mostre quantas palavras
existem nesse arquivo.
Dicas: Use .split() após ler o conteúdo para contar as palavras com len().
"""
conteudo = ""
with open("arquivos.txt","r") as arquivo:
  conteudo = arquivo.read()

qtd_palavras = conteudo.split()
print(f"A quantidade palavras é {len(qtd_palavras)}")