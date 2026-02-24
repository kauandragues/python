with open("pasta/nomes.txt", "w") as arquivo:
    arquivo.write("Ana\nCarlos\nBeatriz")

with open("pasta/nomes.txt","r") as arquivo:
    for linha in arquivo:
        print(linha.strip())