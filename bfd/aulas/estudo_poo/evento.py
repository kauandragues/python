class Evento:
    id = 1
    def __init__(self, nome, local=""):
        self.nome = nome
        self.local = local
        self.id = Evento.id
        Evento.id += 1

    #method de instancia
    def mostrar_dados_do_evento(self):
        print(f"Nome:{self.nome}\n Local:{self.local}")

    #method de classe
    @classmethod
    def criar_evento_online(cls, nome):
        novo_evento = cls(nome, local = f"www.eventos/id={cls.id}.com")
        return novo_evento

    #method static
    @staticmethod
    def evento_eh_bom_com_base_no_numero_de_pessoas(numero_de_pessoas):
        if 50 <= numero_de_pessoas:
            print("Evento eh bom!")
        else:
            print("Evento nao eh bom!")


evento = Evento.criar_evento_online("Evento de Bitcoin")
evento2 = Evento.criar_evento_online("Evento de Macumba")
print(evento.local)
print(evento2.local)
