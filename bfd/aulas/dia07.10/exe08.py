atual = 0
proximo = 1
proximo_do_proximo = 0
#0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
for i in range(11):
    print(atual)
    proximo_do_proximo = atual + proximo
    atual = proximo
    proximo = proximo_do_proximo