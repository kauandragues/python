print("Controle de Acesso por Faixa Etária")
idade = int(input("Digite a sua idade: "))
if idade >= 50:
    print("Você pode ir para a área COMUM, PLUS e VIP")
if idade >= 18:
    print("Você pode ir para área COMUM e PLUS")
if idade >= 16:
    print("Você pode ir para área COMUM")
else:
    print("Você só pode entrar acompanhado de um responsável na área COMUM")