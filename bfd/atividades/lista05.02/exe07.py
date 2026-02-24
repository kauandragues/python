"""
Aluno: github/kauandragues

Exercício 7:
Backup Automático com Data e Hora
Objetivo: Automatizar cópias de segurança.
Descrição: Escreva um programa que crie um backup automático de um arquivo .txt,
adicionando a data e hora ao nome.
Dicas: Use datetime.datetime.now().strftime() e a função shutil.copy()
"""
import datetime, shutil

hora = datetime.datetime.now().strftime("%d-%m-%Y")

try:
  shutil.copy("arquivo.txt",f"{hora}-backup.txt")

except FileNotFoundError:
  print("Arquivo não encontrado!")
  
except Exception as excessao:
  print(f"Erro: {excessao}")

