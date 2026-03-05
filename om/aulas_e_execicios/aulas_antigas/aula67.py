"""
Valores padrão para parametros
Ao definir uma função, os parâmetros podem
ter valores padrão, Caso o valor não seja
enviado para o parâmetro, o valor padrão
será usado.
Refatorar: editar o seu código.
"""


# 0 é Falsy
# Se for definido um valor padrão para um Arg,
# todos os próximos valores precisarão ter um valor padrão
def soma(x, y, z=None):
    if z is not None:
        print(f"{x=} {y=} {z=}", x + y + z)
    else:
        print(f"{x=} {y=}", x + y)


soma(1, 2)
soma(3, 5)
soma(100, 200, 0)
soma(y=10, z=3, x=12)
