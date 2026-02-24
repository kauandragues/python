class Livro:
    def __init__(self, idLivro: int, titulo: str, 
    ISBN: str, ano: int, nomeEditora: str, nomeAutor: str, status: str):
        self.idLivro = idLivro
        self.titulo = titulo
        self.ISBN = ISBN
        self.ano = ano
        self.nomeEditora = nomeEditora
        self.nomeAutor = nomeAutor
        self.status = status

    def __repr__(self) -> str:
        return f"Livro(id={self.idLivro}, titulo='{self.titulo}', autor='{self.nomeAutor}', status='{self.status}')"