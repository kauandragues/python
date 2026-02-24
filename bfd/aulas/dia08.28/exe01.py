class Pessoa:
  def __init__(self, nome, idade, nacionalidade):
    self.nome = nome
    self.idade = idade
    self.nacionalidade = nacionalidade

  def apresentar(self):
    print("--Apresentação--")
    print(f"Esse pessoa se chama {self.nome}")
    print(f"Ela tem {self.idade} anos")
    print(f"E ela é {self.nacionalidade}")

p1 = Pessoa("Kauã",19,"brasileira")
Pessoa.apresentar(p1)