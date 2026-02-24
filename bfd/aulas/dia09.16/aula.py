"""
PEP8 -> boas práticas em python.

Docstrings: help(função) ou print(função.__docstring__)
#Comentários de uma linha para anotações pontuais.

Padrões de Desenvolvimento
MVC/MTV(Django)
abcdefghijklmnopqrstuvwxyz

Princípios SOLID
Single responsability
Open/Closed
Liskov Sbustitution
Interface Segregation
Dependency Inversion

Métodos abstratos

DAO (Data Access Object)
Acessar o banco de dados de forma separada

DRY
don't reapeat yourself

KISS
keep it simple, stupid

Clean Code


Teste Unitários
unittest (ou pytest?)
Mock

CRUD
create
read
update
delete
"""

def saudacao():
  """
  Faz uma saudação
  """
  return "Olá, pessoa!"

print(saudacao.__doc__)
help(saudacao)