print("Calculadora de Desconto Progressivo")
valor_total_compra = float(input("Digite o valor total da compra:R$"))
if valor_total_compra > 500:
    print(f"Valor final com o desconto de 15% (R${valor_total_compra * 0.15:.2f}) deu R${valor_total_compra * 0.85:.2f}")
elif valor_total_compra >= 101:
    print(f"Valor final com o desconto de 10% (R${valor_total_compra * 0.1:.2f}) deu R${valor_total_compra * 0.90:.2f}")
else:
    print(f"Valor final com o desconto de 5% (R${valor_total_compra * 0.5:.2f}) deu R${valor_total_compra * 0.95:.2f}")