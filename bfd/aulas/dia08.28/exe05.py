class ContaBancaria:
  def __init__(self,nome_cliente,numero_da_conta):
    self.nome_cliente = nome_cliente
    self.numero_da_conta = numero_da_conta
    self.quantidade_de_dinheiro = 0

  def depositar(self,quantia=0):
    print("\n--Depositando Dinheiro--")
    print(f"Foram depositados R${quantia:.2f}")
    self.quantidade_de_dinheiro += quantia
    print(f"A quantidade na conta agora é R${self.quantidade_de_dinheiro}")
  
  def sacar(self,quantia=0):
    if quantia == 0:
      print("\nDigite um valor maior que 0!")
    else:
      print("\n--Sacando dinheiro da conta--")
      print(f"A quantia sacada foi de R${quantia}")
      self.quantidade_de_dinheiro -= quantia
      print(f"A quantidade na conta agora é R${self.quantidade_de_dinheiro}")

  def mostrar_detalhes_da_conta(self):
    print("\n--Mostrando informações da conta--")
    print(f"O nome do cliente é {self.nome_cliente}")
    print(f"O número da conta é {self.numero_da_conta}")
    print(f"A quantidade de dinheiro na conta é R${self.quantidade_de_dinheiro:.2f}")

conta1 = ContaBancaria("Kauã",123456)
ContaBancaria.depositar(conta1,100)
conta1.depositar(200)
ContaBancaria.sacar(conta1,200)
conta1.mostrar_detalhes_da_conta()