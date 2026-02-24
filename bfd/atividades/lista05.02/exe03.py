"""
Aluno: github/kauandragues

Função Segura para Abrir Arquivos
Objetivo: Modularizar o tratamento de exceções.
Descrição: Crie uma função que tenta abrir um arquivo e retorna seu conteúdo ou imprime a
mensagem de erro.
Dicas: Use try/except dentro da função, retorne o conteúdo do arquivo se possível.
"""

def ler_arquivo():
  conteudo = []
  try:
    with open("arquivo.txt","r") as arquivo:
      conteudo = arquivo.read()
    return conteudo
  
  except:
    print("Erro na leitura do arquivo!")
    return None
  
#execução principal
if ler_arquivo() is not None: #se o conteudo não foi vazio
  print(ler_arquivo())