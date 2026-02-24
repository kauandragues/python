"""
Aluno: github/kauandragues

Exercício 2:
Verificação de Arquivo Inexistente."
Objetivo: Entender o tratamento de erros ao abrir arquivos.
Descrição: Tente abrir um arquivo 'dados.txt' e trate o erro caso o arquivo não exista.
Dicas: Utilize try/except com FileNotFoundError.
"""
try:
  with open("arquivo.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
except FileNotFoundError:
  print("Arquivo não encontrado :(")

