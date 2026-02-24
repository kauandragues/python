from models.livro import Livro

class LivroDAO:
    def __init__(self, conexao):
        self.conexao = conexao
        self.cursor = conexao.cursor(dictionary=True) 

    def _mapear_para_objeto(self, registro: dict) -> Livro:
        """Converter um registro do DB em um objeto Livro."""

        #cria um objeto livro com os valores passados do registro
        return Livro(
            registro['idLivro'],
            registro['titulo'],
            registro['ISBN'],
            registro['ano'],
            registro['nomeEditora'],
            registro['nomeAutor'],
            registro['status']
        )

    def criar(self, livro: Livro) -> Livro:
        """Realiza um INSERT na tabela livro"""
        query = """
            INSERT INTO livro (titulo, ISBN, ano, nomeEditora, nomeAutor, status) 
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        dados = (livro.titulo, livro.ISBN, livro.ano, livro.nomeEditora, livro.nomeAutor, livro.status)
        
        cursor_normal = self.conexao.cursor()
        cursor_normal.execute(query, dados)
        self.conexao.commit()
        
        livro.idLivro = cursor_normal.lastrowid
        cursor_normal.close()
        return livro

    def buscar_todos(self) -> list[Livro]:
        """Realiza o SELECT de todos os livros"""
        query = "SELECT * FROM livro"
        self.cursor.execute(query)
        registros = self.cursor.fetchall()
        return [self._mapear_para_objeto(reg) for reg in registros]

    def buscar_por_id(self, id_livro: int) -> Livro | None:
        """Realiza o SELECT por id na tabela de livro"""
        query = "SELECT * FROM livro WHERE idLivro = %s"
        self.cursor.execute(query, (id_livro,))
        
        registro = self.cursor.fetchone()
        if registro:
            return self._mapear_para_objeto(registro)
        return None

    def atualizar_status(self, livro: Livro, novo_status: str):
        """Atualiza o status do livro 'Emprestado' ou 'Disponível'"""
        livro.status = novo_status
        query = "UPDATE livro SET status = %s WHERE idLivro = %s"
        dados = (novo_status, livro.idLivro)
        
        cursor_normal = self.conexao.cursor()
        cursor_normal.execute(query, dados)
        self.conexao.commit()
        cursor_normal.close()
    
    def buscar_por_status(self, status: str) -> list[Livro]:
        """Busca livros por 'Disponível' ou 'Emprestado'."""
        query = "SELECT * FROM livro WHERE status = %s"
        self.cursor.execute(query, (status,))
        registros = self.cursor.fetchall()

        #mapeia o registro para um objeto, e retorna essa lista de objetos no final
        return [self._mapear_para_objeto(reg) for reg in registros]

    def buscar_por_titulo_parcial(self, titulo: str) -> list[Livro]:
        """Busca livros usando títulos parciais."""
        query = "SELECT * FROM livro WHERE titulo LIKE %s"
        valor_busca = f"%{titulo}%"
        self.cursor.execute(query, (valor_busca,))
        registros = self.cursor.fetchall()

        #mapeia o registro para um objeto, e retorna essa lista de objetos no final
        return [self._mapear_para_objeto(reg) for reg in registros]

    def buscar_por_ano(self, ano: int) -> list[Livro]:
        """Busca livros por ano exato de publicação."""
        query = "SELECT * FROM livro WHERE ano = %s"
        self.cursor.execute(query, (ano,))
        registros = self.cursor.fetchall()

        #mapeia o registro para um objeto, e retorna essa lista de objetos no final
        return [self._mapear_para_objeto(reg) for reg in registros]