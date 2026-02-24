lista_palavras = []

#guardar todas as palavras do usuario
print("Palavras com mais de 5 letras")
for palavra in range(5):
  lista_palavras.append(input("Digite uma palavra para ser colocada na lista:"))

#imprimir palavras que possuem maiores que 5 letras
for palavra in lista_palavras:
  if len(palavra) >= 5:
    print(palavra)

