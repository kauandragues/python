salario = float(input("Digite o seu salário:"))
dias_ferias = int(input("Digite a quantidade de dias de férias:"))
valor_ferias = salario*(dias_ferias/30)
terco = valor_ferias/3
total = valor_ferias+terco
print(f"O valor que será recebido é R${total:.2f}")