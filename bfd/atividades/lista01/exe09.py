print("Validação de Login")
usuario = input("Digite seu usuário: ")
senha = input("Digite sua senha: ")
if usuario == "admin" and senha =="1234":
    print("Parabéns, senha e usuários corretos!")
else:
    print("Senha ou usuário incorretos!")