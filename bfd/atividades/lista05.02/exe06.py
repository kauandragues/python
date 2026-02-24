"""
Aluno: github/kauandragues

Gerador de Log de Erros de Arquivo
Objetivo: Registrar erros em log.
Descrição: Crie um programa que tenta abrir arquivos e grava os erros em um arquivo
log.txt.
Dicas: Use with open("log.txt", "a") dentro do except para registrar a
mensagem.
"""

try: 
    with open("texto.txt", "r") as arquivo: 
        conteudo = arquivo.read() 

except FileNotFoundError as excessao: 
    with open("log.txt", "a") as arquivo_log: 
        arquivo_log.write(f"Erro ao tentar abrir o arquivo: {excessao}\n")