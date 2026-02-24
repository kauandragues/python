from datetime import datetime
print("Agenda Inteligente")
nome = input("Digite seu nome: ")
data_aniversario = input("Digite o seu a data do seu aniversário (dd/mm/ano): ")
dia_da_semana_aniversario = datetime.strptime(data_aniversario,'%d/%m/%Y').weekday()

if dia_da_semana_aniversario == 0:
    print(f"Olá, {nome}! O dia da semana do seu aniversário é SEGUNDA-FEIRA")
elif dia_da_semana_aniversario == 1:
    print(f"Olá, {nome}! O dia da semana do seu aniversário é TERÇA-FEIRA")
elif dia_da_semana_aniversario == 2:
    print(f"Olá, {nome}! O dia da semana do seu aniversário é QUARTA-FEIRA")
elif dia_da_semana_aniversario == 3:
    print(f"Olá, {nome}! O dia da semana do seu aniversário é QUINTA-FEIRA")
elif dia_da_semana_aniversario == 4:
    print(f"Olá, {nome}! O dia da semana do seu aniversário é SEXTA-FEIRA")
elif dia_da_semana_aniversario == 5:
    print(f"Olá, {nome}! O dia da semana do seu aniversário é SÁBADO")
elif dia_da_semana_aniversario == 6:
    print(f"Olá, {nome}! O dia da semana do seu aniversário é DOMINGO")
