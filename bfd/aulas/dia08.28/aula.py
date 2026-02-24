"""
PROGRAMAÇÃO ORIENTADA A OBJETOS
"""
class Pessoa:
  def __init__(self, nome, idade):
    self.nome = nome
    self.idade = idade

  def apresentar(self):
    print(f"Esse é o(a) {self.nome} e ele(a) tem {self.idade}")

pessoa1 = Pessoa("João", 25)
pessoa2 = Pessoa("Maria", 30)

pessoa1.apresentar();

