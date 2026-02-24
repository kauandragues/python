from models.emprestimo import Emprestimo
from models.livro import Livro
from models.usuario import Usuario

class EmprestimoDAO:
    def __init__(self, conexao):
        self.conexao = conexao
        self.cursor = conexao.cursor(dictionary=True)

    def _mapear_para_objeto(self, registro: dict) -> Emprestimo:
        """Converter os registros em objetos"""
        livro = Livro(
            registro['idLivro'], registro['titulo'], registro['ISBN'],
            registro['ano'], registro['nomeEditora'], 
            registro['nomeAutor'], registro['livro_status']
        )
        usuario = Usuario(
            registro['matriculaUsuario'], registro['nome'], 
            registro['email']
        )
        emprestimo = Emprestimo(
            registro['idEmprestimo'], livro, usuario,
            registro['dataRetirada'],
            registro['dataDevolucaoPrevista'],
            registro['dataDevolucaoReal'],
            registro['status']
        )
        return emprestimo

    def criar(self, emprestimo: Emprestimo) -> Emprestimo:
        """Cria um empréstimo e realiza a query no banco"""
        query = """
            INSERT INTO emprestimo 
            (dataRetirada, dataDevolucaoPrevista, dataDevolucaoReal, status, idLivro, matriculaUsuario) 
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        dados = (
            emprestimo.dataRetirada, emprestimo.dataDevolucaoPrevista, 
            emprestimo.dataDevolucaoReal, emprestimo.status, 
            emprestimo.livro.idLivro, emprestimo.usuario.matriculaUsuario
        )
        
        cursor_normal = self.conexao.cursor()
        cursor_normal.execute(query, dados)
        self.conexao.commit()
        
        emprestimo.idEmprestimo = cursor_normal.lastrowid
        cursor_normal.close()
        return emprestimo

    def buscar_por_id(self, id_emprestimo: int) -> Emprestimo | None:
        """Realiza o SELECT no por id do empréstimo"""
        query = """
            SELECT e.*, 
                   l.titulo, l.ISBN, l.ano, l.nomeEditora, l.nomeAutor, l.status as livro_status,
                   u.nome, u.email
            FROM emprestimo e
            JOIN livro l ON e.idLivro = l.idLivro
            JOIN usuario u ON e.matriculaUsuario = u.matriculaUsuario
            WHERE e.idEmprestimo = %s
        """
        self.cursor.execute(query, (id_emprestimo,))
        
        registro = self.cursor.fetchone()
        if registro:
            return self._mapear_para_objeto(registro)
        return None

    def atualizar_devolucao(self, emprestimo: Emprestimo):
        """Realiza um UPDATE na tabela de empréstimo para a devolução"""
        query = "UPDATE emprestimo SET dataDevolucaoReal = %s, status = %s WHERE idEmprestimo = %s"
        dados = (emprestimo.dataDevolucaoReal, emprestimo.status, emprestimo.idEmprestimo)
        
        cursor_normal = self.conexao.cursor()
        cursor_normal.execute(query, dados)
        self.conexao.commit()
        cursor_normal.close()
    
    def atualizar_status_automatico(self) -> int:
        """
        Atualiza todos os empréstimos pendentes para 'Atrasado' se a data atual for maior que a data prevista.
        """
        query = """
            UPDATE emprestimo 
            SET status = 'Atrasado' 
            WHERE dataDevolucaoPrevista < CURDATE() 
              AND dataDevolucaoReal IS NULL
              AND status != 'Atrasado'
        """
        cursor_normal = self.conexao.cursor()
        cursor_normal.execute(query)
        self.conexao.commit()
        
        # retorna o número de linhas afetadas
        num_linhas_afetadas = cursor_normal.rowcount
        cursor_normal.close()
        return num_linhas_afetadas

    def buscar_ativos(self) -> list[Emprestimo]:
        """Busca todos os empréstimos que ainda não foram devolvidos."""
        query = """
            SELECT e.*, 
                   l.titulo, l.ISBN, l.ano, l.nomeEditora, l.nomeAutor, l.status as livro_status,
                   u.nome, u.email
            FROM emprestimo e
            JOIN livro l ON e.idLivro = l.idLivro
            JOIN usuario u ON e.matriculaUsuario = u.matriculaUsuario
            WHERE e.dataDevolucaoReal IS NULL
            ORDER BY e.dataDevolucaoPrevista ASC
        """
        self.cursor.execute(query)
        registros = self.cursor.fetchall()
        return [self._mapear_para_objeto(reg) for reg in registros]

    def buscar_devolvidos(self) -> list[Emprestimo]:
        """Busca todos os empréstimos que já foram devolvidos."""
        query = """
            SELECT e.*, 
                   l.titulo, l.ISBN, l.ano, l.nomeEditora, l.nomeAutor, l.status as livro_status,
                   u.nome, u.email
            FROM emprestimo e
            JOIN livro l ON e.idLivro = l.idLivro
            JOIN usuario u ON e.matriculaUsuario = u.matriculaUsuario
            WHERE e.dataDevolucaoReal IS NOT NULL
            ORDER BY e.dataDevolucaoReal DESC
        """
        self.cursor.execute(query)
        registros = self.cursor.fetchall()
        return [self._mapear_para_objeto(reg) for reg in registros]