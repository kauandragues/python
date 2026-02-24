from models.usuario import Usuario

class UsuarioDAO:
    def __init__(self, conexao):
        self.conexao = conexao
        self.cursor = conexao.cursor()

    def criar(self, usuario: Usuario) -> Usuario:
        """Realiza um INSERT na tabela de usuário"""
        query = "INSERT INTO usuario (nome, email) VALUES (%s, %s)"
        dados = (usuario.nome, usuario.email)
        
        self.cursor.execute(query, dados)
        self.conexao.commit()
        
        usuario.matriculaUsuario = self.cursor.lastrowid
        return usuario

    def buscar_todos(self) -> list[Usuario]:
        """Realiza um SELECT na tabela de usuário para buscar todos os usuários"""
        query = "SELECT matriculaUsuario, nome, email FROM usuario"
        self.cursor.execute(query)
        
        registros = self.cursor.fetchall()
        
        lista_usuarios = []
        for (matricula, nome, email) in registros:
            usuario = Usuario(matriculaUsuario=matricula, nome=nome, email=email)
            lista_usuarios.append(usuario)
            
        return lista_usuarios

    def buscar_por_matricula(self, matricula: int) -> Usuario | None:
        """Realiza um SELECT do na tablea de usuário para buscar usuário por matricula"""
        query = "SELECT matriculaUsuario, nome, email FROM usuario WHERE matriculaUsuario = %s"
        self.cursor.execute(query, (matricula,))
        
        registro = self.cursor.fetchone()
        if registro:
            (matricula_bd, nome, email) = registro
            return Usuario(matriculaUsuario=matricula_bd, nome=nome, email=email)
        return None