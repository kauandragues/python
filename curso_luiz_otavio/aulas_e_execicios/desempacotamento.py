nome1, nome2, nome3 = ["pedro", "maria", "jose"]

print(nome1, nome2, nome3)

nome1, *_ = ["pedro", "maria", "jose"]
print(nome1, _)

lista = ["pedro", "maria", "jose"]
print(*lista)

string = "abcdef"
print(*string)