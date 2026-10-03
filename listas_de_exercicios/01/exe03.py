dividendo = 0
divisor = 0
resultado_divisao = 0
resultado_divisao_inteira = 0
resultado_resto = 0

while(dividendo == 0 or divisor == 0):
    try:
        dividendo = int(input("Digite o dividendo:"))
        divisor = int(input("Digite o divisor:"))
        
        resultado_divisao = dividendo / divisor
        resultado_divisao_inteira = dividendo // divisor
        resultado_resto = dividendo % divisor
    except TypeError:
            print("Tipo de dado inválido")    
    except ZeroDivisionError: 
        print("Divisão por zero não é possível")
    
print(f"{dividendo} / {divisor} = {resultado_divisao} | tipo: {type(resultado_divisao).__name__}")
print(f"{dividendo} // {divisor} = {resultado_divisao_inteira} | tipo: {type(resultado_divisao_inteira).__name__}")
print(f"{dividendo} % {divisor} = {resultado_resto} | tipo: {type(resultado_resto).__name__}")
