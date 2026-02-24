class ContaBancaria:
  def __init__(self, numero_da_conta,nome_cliente,saldo=0):
    self.__numero_da_conta = numero_da_conta
    self.__nome_cliente = nome_cliente
    self.__saldo = saldo

  def depositar(self,valor=0):
    print("\n--Depositar valor--")

    try:
      valor = float(valor)
    except ValueError:
      print("Você não digitou um número!")
      return
    
    self.__saldo += valor
    print(f"Você depositou R${valor:.2f} com sucesso!")
  
  def sacar(self,valor=0):
    print("\n--Sacando valor--")

    try:
      valor = float(valor)
    except ValueError:
      print("Você não digitou um número!")
      return
    
    #valida se tem dinheiro para realizar esse saque
    if self.__saldo - valor < 0:
      print("Não há dinheiro suficiente na sua conta para realizar esse saque!")
      return

    self.__saldo -= valor    
    print(f"Você sacou R${valor} com sucesso!")

  def __str__(self):
    return (f"\n--Mostra informações da conta--"
          f"\nNúmero da conta:{self.__numero_da_conta}"
          f"\nNome do cliente:{self.__nome_cliente}"
          f"\nSaldo da conta:R${self.__saldo}")

cliente1 = ContaBancaria(12345,"Kauã")
cliente1.depositar(100)
print(cliente1)
cliente1.sacar(50)
print(cliente1)
cliente1.sacar(100)
print(cliente1)
