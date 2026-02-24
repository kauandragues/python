class Evento:
    def __init__(self, atributo):
        self.atributo = atributo
        self.atributo2 = "atributor2"
    
    #método de instância
    def __str__(self):
        return self.atributo + self.atributo2

    @staticmethod
    def mostrar_estatico():
        return "meotodo estático"

    @classmethod
    def mostrar_classmetodo(cls):
        return "meotodo classe"
 
print(Evento("atributo1 "))
print()
print(Evento.mostrar_estatico())
print()
print(Evento.mostrar_classmetodo())
