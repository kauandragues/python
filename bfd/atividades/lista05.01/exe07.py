"""
Aluno: github/kauandragues

"""

try:
    with open("texto.txt", "r") as arquivo:
        conteudo = arquivo.read()
except FileNotFoundError as excessao:
    with open("log_erros.txt", "a") as arquivo_log:
        arquivo_log.write(f"Erro ao tentar abrir o arquivo: {excessao}\n")
