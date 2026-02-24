"""
Aluno: github/kauandragues

Menu Interativo 
Objetivo: Aplicar while com controle de menu. 
Descrição: Crie um menu com opções (1) Ver lista, (2) Adicionar item, (0) Sair. 
Use while com condição e input() para opções 
"""
lista_itens = []
while True:
  print("\n==================================")
  print("\nBem-Vindo ao Menu de Itens\n")
  print("1 - Ver lista")
  print("2 - Adicionar item")
  print("0 - Sair\n")
  opcao = int(input("Digite uma opção (ex: 1):"))

  #caso seja a opcao 0
  if opcao == 0:
    print("\nAté a próxima!")
    break; #quebra o loop
  
  #caso seja a opcao 1
  elif opcao == 1:
    if len(lista_itens) > 0: #se a lista estiver vazia
      print("\nImprimindo Lista de Itens!\n")
      for item in lista_itens:
        print(item)
    else:
      print("Lista de itens está vazia!")

  #caso seja a opcao 2
  elif opcao == 2: 
    print("\nAdicionando um Item na Lista!")
    item_usuario = input("Digite o item que deseja adicionar:")
    lista_itens.append(item_usuario)#adicionando item no final da lista

