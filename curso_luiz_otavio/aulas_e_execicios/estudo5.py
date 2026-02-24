velocidade = 61
local_carro = 90

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

distacia_carro_radar = abs(local_carro - LOCAL_1)

if distacia_carro_radar <= RADAR_RANGE:
    print("Está no range do radar")
    if velocidade > RADAR_1:
        print("Passou da velocidade máxima")
    