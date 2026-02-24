class Usuario:
    def __init__(self, matriculaUsuario: int, nome: str, email: str):
        self.matriculaUsuario = matriculaUsuario
        self.nome = nome
        self.email = email

    def __repr__(self) -> str:
        return f"Usuario(matricula={self.matriculaUsuario}, nome='{self.nome}', email='{self.email}')"