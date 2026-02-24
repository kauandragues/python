class Produto:
  def __init__(self,nome,preco,frete,imposto):
    self.nome = nome
    self.preco = preco
    self.frete = frete
    self.imposto = imposto

  def calcular_imposto_em_reais(self):
    return (self.preco + self.frete)*((self.imposto/100))

  def calcular_valor_total(self):
    return self.preco + self.frete + self.calcular_imposto_em_reais()

  def apresentar_valor_total(self):
    print(f"--Apresentação do valor total do {self.nome}--")
    print(f"O valor total é de R${self.calcular_valor_total():.2f}")

p1 = Produto("Lápis",0.5,2,15)
Produto.apresentar_valor_total(p1)
