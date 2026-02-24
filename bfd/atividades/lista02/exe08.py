tentativas = 3
while tentativas > 0:
    login = input("Digite seu login: ")
    senha = input("Digite sua senha: ")
    if login == "admin" and senha == "1234":
        print("Parabéns!! Você entrou com sucesso.")
        tentativas = 0
    else:
        tentativas-=1
        if tentativas == 0:
            print("Você gastou todas as suas tentativas, acesso negado!")
        else:
            print(f"Senha ou Login incorretos, tentativa faltando {tentativas}")