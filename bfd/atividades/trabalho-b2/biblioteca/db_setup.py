import mysql.connector
from mysql.connector import errorcode
from config import DB_CONFIG

# inicializar o banco de dados se ele não existir
# também criar as tabelas do banco
# e colocar alguns registros

TABELAS = {}

# todos os sql são do arquivo de forward engineer do workbench kk

TABELAS['usuario'] = """
    CREATE TABLE IF NOT EXISTS usuario (
        matriculaUsuario INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(255) NOT NULL,
        email VARCHAR(255) UNIQUE
    );"""

TABELAS['livro'] = """
    CREATE TABLE IF NOT EXISTS livro (
        idLivro INT AUTO_INCREMENT PRIMARY KEY,
        titulo VARCHAR(255) NOT NULL,
        ISBN VARCHAR(20) UNIQUE,
        ano INT,
        nomeEditora VARCHAR(100),
        nomeAutor VARCHAR(255),
        status VARCHAR(20) NOT NULL DEFAULT 'Disponível'
    );"""

TABELAS['emprestimo'] = """
    CREATE TABLE IF NOT EXISTS emprestimo (
        idEmprestimo INT AUTO_INCREMENT PRIMARY KEY,
        dataRetirada DATE NOT NULL,
        dataDevolucaoPrevista DATE NOT NULL,
        dataDevolucaoReal DATE NULL,
        status VARCHAR(20),
        idLivro INT NOT NULL,
        matriculaUsuario INT NOT NULL,
        
        FOREIGN KEY (idLivro) REFERENCES livro(idLivro),
        FOREIGN KEY (matriculaUsuario) REFERENCES usuario(matriculaUsuario)
    );"""

def criar_banco(cursor, nome_banco):
    """Cria o banco de dados no mysql"""
    # sql do foward engineer do mysql workbench
    try:
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS `{nome_banco}` CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_unicode_ci'")
    except mysql.connector.Error as err:
        print(f"Falha ao criar banco de dados: {err}")
        exit(1)

def criar_tabelas(cursor):
    """Cria as tabelas usuario, emprestimo e livro"""
    for nome_tabela in TABELAS:
        sql_tabela = TABELAS[nome_tabela]
        try:
            cursor.execute(sql_tabela)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("já existe.")
            else:
                print(f"\nFalha: {err.msg}")

def popular_banco(cursor, conexao):
    """Realiza os INSERTs no banco de dados para ter exemplos de usuários, livros e empréstimos"""
    # colocas os registros básicos no banco
    try:
        cursor.execute("SELECT COUNT(*) FROM usuario")
        if cursor.fetchone()[0] == 0:
            
            #colocar os usuários no banco
            sql_usuarios = "INSERT INTO usuario (nome, email) VALUES (%s, %s)"
            dados_usuarios = [
                ('Carlos Silva', 'carlos.silva@email.com'), ('Mariana Costa', 'mariana.costa@email.com'),
                ('Fernando Pereira', 'fernando.pereira@email.com'), ('Juliana Santos', 'juliana.santos@email.com'),
                ('Rafael Oliveira', 'rafael.oliveira@email.com'), ('Kauã de Andrade', 'kaua.rodrigues@gmail.com'),
            ]
            cursor.executemany(sql_usuarios, dados_usuarios)

            # colocar os livros no banco
            sql_livros = "INSERT INTO livro (titulo, ISBN, ano, nomeEditora, nomeAutor, status) VALUES (%s, %s, %s, %s, %s, %s)"
            dados_livros = [
                ('O Senhor dos Anéis', '9788532519428', 1954, 'HarperCollins', 'J.R.R. Tolkien', 'Emprestado'),
                ('Dom Quixote', '9788525416075', 1605, 'Penguin Books', 'Miguel de Cervantes', 'Disponível'),
                ('Cem Anos de Solidão', '9788532522145', 1967, 'Record', 'Gabriel García Márquez', 'Emprestado'),
                ('A Arte da Guerra', '9788572836269', -500, 'Jardim dos Livros', 'Sun Tzu', 'Disponível'),
                ('1984', '9788535914849', 1949, 'Companhia das Letras', 'George Orwell', 'Disponível'),
                ('O Vilarejo', '9788581053059', 2015, 'Suma', 'Raphael Montes', 'Disponível'),
            ]
            cursor.executemany(sql_livros, dados_livros)

            # colocar os empréstimos no banco
            sql_emprestimos = """
                INSERT INTO emprestimo (dataRetirada, dataDevolucaoPrevista, dataDevolucaoReal, status, idLivro, matriculaUsuario) 
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            dados_emprestimos = [
                ('2025-08-01', '2025-08-08', '2025-08-08', 'Dentro do Prazo', 3, 2),
                ('2025-08-05', '2025-08-12', None, 'Atrasado', 1, 5),
                ('2025-08-10', '2025-08-17', '2025-08-19', 'Atrasado', 5, 1),
                ('2025-08-20', '2025-08-26', '2025-08-27', 'Atrasado', 2, 3),
                ('2025-08-25', '2025-09-01', None, 'Atrasado', 4, 4),
                ('2025-08-27', '2025-09-03', None, 'Atrasado', 3, 4)
            ]
            cursor.executemany(sql_emprestimos, dados_emprestimos)
            
            conexao.commit()
            
    except mysql.connector.Error as err:
        print(f"\nErro ao colocar os registros no banco de dados: {err}")
        conexao.rollback()

def inicializar_banco():
    """Executar cada um dos passos para a criação do banco de dados
    Retornar a conexão para o banco"""

    conexao_bd = None
    try:
        config_copia = DB_CONFIG.copy()
        nome_banco = config_copia.pop('database') 
        
        conexao_servidor = mysql.connector.connect(**config_copia)
        cursor = conexao_servidor.cursor()
        criar_banco(cursor, nome_banco)
        cursor.close()
        conexao_servidor.close()
        
        conexao_bd = mysql.connector.connect(**DB_CONFIG)
        cursor = conexao_bd.cursor()
        criar_tabelas(cursor)
        popular_banco(cursor, conexao_bd)
        cursor.close()
        
        return conexao_bd

    except mysql.connector.Error as err:
        print(f"Erro no setup do banco de dados: {err}")
    
        if conexao_bd:
            conexao_bd.close()
        return None