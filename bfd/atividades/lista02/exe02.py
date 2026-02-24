print("Conversor de Moedas")
taxa_dolar = 0.2
taxa_iene = 174
taxa_euro = 0.15
reais = float(input("Digite um valor em R$"))
print(f"R${reais} em dolares é ${reais*taxa_dolar:.2f}")
print(f"R${reais} em euro é €{reais*taxa_euro:.2f}")
print(f"R${reais} em iene é ¥{reais*taxa_iene:.2f}")

