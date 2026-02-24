from datetime import date
from .livro import Livro
from .usuario import Usuario

class Emprestimo:
    def __init__(self, idEmprestimo: int, livro: Livro, usuario: Usuario, 
                 dataRetirada: date, dataDevolucaoPrevista: date, 
                 dataDevolucaoReal: date | None, status: str):
        
        self.idEmprestimo = idEmprestimo
        self.livro = livro
        self.usuario = usuario
        self.dataRetirada = dataRetirada
        self.dataDevolucaoPrevista = dataDevolucaoPrevista
        self.dataDevolucaoReal = dataDevolucaoReal
        self.status = status

    def __repr__(self) -> str:
        return (f"Emprestimo(id={self.idEmprestimo}, "
                f"livro_id={self.livro.idLivro}, "
                f"usuario_matricula={self.usuario.matriculaUsuario}, "
                f"status='{self.status}')")