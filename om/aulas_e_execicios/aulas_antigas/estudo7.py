horario = input("Digite o horário atual (ex: 22:45): ")

hora = horario.split(":")[0]
minuto = horario.split(":")[1]

try:
    hora = int(hora)
    minuto = int(minuto)
    
    if hora >= 0 and hora <= 11:
        print(f"Bom dia, {hora:02}:{minuto:02}")
    elif hora >=12 and hora <= 17:
        print(f"Boa tarde, {hora:02}:{minuto:02}")
    elif hora >= 18 and hora < 24:
        print(f"Boa noite, {hora:02}:{minuto:02}")
    else:
        print("Esse horário não existe!")
except:
    print("O horário digitado não foi aceito")