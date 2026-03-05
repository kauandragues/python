def main():
    lista_cpf = []
    digitos_cpf = []
    primeiro_digito_correto = None
    segundo_digito_correto = None

    cpf = input("Digite o seu CPF:")

    # colocar cada um dos números em uma lista
    for i, c in enumerate(cpf):
        if not c.isdigit():
            continue
        elif c.isdigit() and len(cpf) - 1 == i or len(cpf) - 2 == i:
            digitos_cpf.append(c)
        else:
            lista_cpf.append(c)
    # ============================================

    # multiplicar a partir do dois cada um dos números de tŕas pra frente
    # e somar o resultado
    soma = 0
    multiplicador = 2
    for num in lista_cpf[::-1]:
        soma = soma + (int(num) * multiplicador)
        multiplicador = multiplicador + 1

    # ============================================

    # dividimos o resultado por 11
    # se o resto da divisão for < 2, então é 0
    # se não o primeiro digito verificador é 11 - resto

    resto_primeiro_digito = soma % 11
    if resto_primeiro_digito < 2:
        primeiro_digito_correto = 0
    elif resto_primeiro_digito >= 2:
        primeiro_digito_correto = 11 - resto_primeiro_digito

    # Termina a descoberta do primeiro dígito
    # ====================================================================

    # adicionamos o digito ao cpf e refazemos a mesma conta do primeiro dígito
    lista_cpf.append(primeiro_digito_correto)

    soma = 0
    multiplicador = 2
    for num in lista_cpf[::-1]:
        soma = soma + (int(num) * multiplicador)
        multiplicador = multiplicador + 1

    resto_segundo_digito = soma % 11
    if resto_segundo_digito < 2:
        segundo_digito_correto = 0
    elif resto_segundo_digito >= 2:
        segundo_digito_correto = 11 - resto_segundo_digito

    # Final da descoberta do segundo dígito
    # ===========================================================

    # Verificar se o cpf é válido e mostrar qual seria o válido se não for
    primeiro_digito = int(digitos_cpf[0])
    segundo_digito = int(digitos_cpf[1])
    if (
        primeiro_digito == primeiro_digito_correto
        and segundo_digito == segundo_digito_correto
    ):
        print("o cpf é válido")
    else:
        print("o cpf não é válido")
        lista_cpf.append(segundo_digito_correto)
        print("cpf correto:","".join(lista_cpf))
if __name__ == "__main__":
    main()
