"""
Args nomeados e não nomeados em def python
args nomeados tem nome=
args não nomeados tem apenas o valor
"""


# funções em python por padrão retornam None
def soma(x, y):  # Parâmetros são na definição da função
    print(f"{y} + {x} = x + y")


soma(x=1, y=2)  # Argumento são na chamada da função
soma(y=2, x=1)
