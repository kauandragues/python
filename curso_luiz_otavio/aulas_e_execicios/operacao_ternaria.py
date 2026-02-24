print("valor" if True else "outro valor")
print("valor" if False else "outro valor")

condicao = 10 == 10
variavel = "valor" if condicao else "outro valor"
print(variavel)

digito = 9
digito = digito if digito <= 9 and digito >= 0 else 0
digito = 0 if digito > 9 or digito < 0 else digito
print(digito)