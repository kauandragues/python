import datetime
ano_atual = datetime.datetime.now().year
print("Calcular a idade com base no ano de nascimento")
ano_nascimento = int(input("Digite o ano em que você nasceu: "))
idade = ano_atual - ano_nascimento
if idade >= 18:
    print(f"Você tem {idade} anos e é maior de idade")
else:
    print(f"Você tem {idade} anos e é menor de idade")