def soma(a: int, b: int) -> None: 
  """
  Descrição: 
  Soma dois números
  
  Argumento: 
  a(int) é um dos números que serão somados
  b(int) é um dos números que serão somados

  Retorno: 
  Retorna o resultado da soma
  """
  return a+b

def subtracao(a: int, b: int) -> None: 
  """
  Descrição: 
  Subtrai dois números
  
  Argumento: 
  a(int) é o número que terá ser valor subtraido
  b(int) é o número que subtrairá o valor de a

  Retorno: 
  Retorna o resultado da subtração(int)
  """
  return a-b

def calcular_media(lista_de_numeros: list) -> float: 
  """
  Descrição: 
  Calcula a média de uma lista números

  Argumento: 
  lista_de_numeros(list) é a lista com todos os números

  Retorno: 
  Retorna a média da lista de números(float) 
  """
  return sum(lista_de_numeros) / len(lista_de_numeros)

