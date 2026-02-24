class Aluno:
  def __init__(self,nome,prova1,prova2):
    self.nome = nome
    self.prova1 = prova1
    self.prova2 = prova2

  def lista_notas(self):
    print("\n--Listagem de Notas--")
    print(f"O aluno {self.nome} tirou:")
    print(f"Prova 1 -> {self.prova1:.2f}")
    print(f"Prova 2 -> {self.prova2:.2f}")

  def media(self):
    print("\n--Apresentação da média--")
    print(f"Para o aluno {self.nome}")
    print(f"A média é {(self.prova1 + self.prova2) / 2}")


aluno1 = Aluno("Kauã",7.0,9.0)
Aluno.lista_notas(aluno1)
Aluno.media(aluno1)