"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local podem ser alcançados.
"""


def escopo():
    x = 1  # Está definida dentro da função, ou seja, está dentro do escopo da função
    print(x)


# não é possivel alcançar x fora da função, porque ela está dentro da função
# print(x) não funciona
escopo()

# -----------------------------------------------------------------------------------------
x = 1  # escopo do módulo


def escopo1():
    y = 2

    def outro_escopo():
        print(x, y)  # É possível acessar os escopos acima, mas aquele dentro não.
        # x está no escopo global/modulo
        # y está no escopo da primeira função
        # mesmo assim é possível acessa-los

    outro_escopo()
    print(x)


print()
escopo1()

# -----------------------------------------------------------------------------------------
x = 1


def escopo2():
    x = 10

    def outro_escopo():
        x = 20
        y = 2
        print(x, y)

    outro_escopo()
    print(x)


print()
print(x)  # vai ir no x no escopo global
escopo2()  # vai printar o x do escopo da função
print(x)  # vai ir no x no escopo global

# -----------------------------------------------------------------------------------------
x = 1


def escopo3():
    global x  # fala para referenciar o x que está no escopo acima
    x = 10  # altera o valor do x do escopo acima para 10

    def outro_escopo1():
        x = 20  # cria um x novo para esse escopo, não tem relação com o x do escopo acima
        y = 2
        print(x, y)

    outro_escopo1()
    print(x)


print()
print(x)
escopo3()
print(x)
