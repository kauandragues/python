nome_global = "nome_global"

def func_global() -> None:
    nome_enclosing = "Foda" # Enclosing (Local)

    def func_interna() -> None:
        nonlocal nome_enclosing
        nome_enclosing = "MUDAR"
        print(nome_enclosing, id(nome_enclosing))

    print(nome_enclosing, id(nome_enclosing))
    func_interna()

func_global()