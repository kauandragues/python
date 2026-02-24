import decimal

num1 = 0.1
num2 = 0.7
num3 = num1 + num2
print(num3)
print(f"{num3:.2f}")
print(round(num3, 2))

num1 = decimal.Decimal("0.1")
num2 = decimal.Decimal("0.7")
num3 = num1 + num2
print(num3)