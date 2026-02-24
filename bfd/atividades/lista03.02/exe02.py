tentativas = 1 

while True: 
  usuario = input("Digite o seu usuário:") 
  senha = input("Digite a sua senha:") 
  if tentativas >= 3: 
    print("Acesso negado! Você tentou 3 vezes!") 
    break; 
  else: 
    if usuario == "admin" and senha == "12345": 
      print("Parabéns! Você entrou com sucesso!") 
      break; 
    else: 
      print(f"Senha ou Usuário incorretos! Você tentou {tentativas} tentativas!") 
      tentativas += 1 