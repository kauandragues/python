class Carro:
  def __init__(self,modelo,ano,fabricante):
    self.modelo = modelo
    self.ano = ano
    self.fabricante = fabricante
    self.velocidade = 0

  def mostrar_dados_carro(self):
    print("\n--Mostrar informações do Carro--")
    print(f"O modelo é {self.modelo}")
    print(f"O ano é {self.ano}")
    print(f"O fabricante é {self.fabricante}")

  def acelerar(self,incremento=10):
    if self.velocidade + incremento >= 300:
      print("\nO carro está a 300km/h, o limite dele!!")
    else:
      self.velocidade += incremento
      print("\nO carro está acelerando!")
      print(f"A velocidade atual do carro é {self.velocidade}")

  def frear(self,decremento=10):
    if self.velocidade - decremento <= 0:
      print("\nO carro está parado");
    else:
      self.velocidade -= decremento
      print("\nO carro está freando!")
      print(f"A velocidade atuald do carro é {self.velocidade}")

carro1 = Carro("Fusca", 1938, "Volkswagen")
Carro.mostrar_dados_carro(carro1)
Carro.acelerar(carro1,10)
Carro.frear(carro1,5)
Carro.acelerar(carro1,30)
Carro.frear(carro1,100)