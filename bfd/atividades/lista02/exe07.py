distancia = float(input("Digite a distância em km: "))
velo_media = float(input("Digite a velocidade média em km/h: "))
print("O tempo estimado de viagem é de",int(distancia/velo_media),"h",int(60*((distancia/velo_media)-int(distancia/velo_media))),"min")

