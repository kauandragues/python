import calculadora

def main(): 

    #exe1
    a = 10
    b = 20
    
    soma      = calculadora.soma(a,b)
    subtracao = calculadora.subtracao(a,b)

    print(calculadora.soma.__doc__)
    print(soma)

    print(calculadora.subtracao.__doc__)
    print(subtracao)

    #exe2
    lista_de_numeros = [1,2,3,4,5]

    media = calculadora.calcular_media(lista_de_numeros)

    print(calculadora.calcular_media.__doc__)
    print(media)

if __name__ == "__main__":
  main()
