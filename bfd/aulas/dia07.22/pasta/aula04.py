notas = {"Ana": 8.5, "Carlos": 6.7, "Beatriz":9.0}
with open("relatorio.txt","w") as arquivo:
    arquivo.write("Relatório de Notas\n")
    arquivo.write("=====================\n")
    for nome, nota in notas.items():
        status = "Aprovado" if nota >= 7 else "Reprovado"
        arquivo.write(f"{nome}: {nota} - {status}\n")