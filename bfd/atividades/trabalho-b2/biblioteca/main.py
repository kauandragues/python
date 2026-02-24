import mysql.connector
from controllers.biblioteca_controller import BibliotecaController
from db_setup import inicializar_banco

def executar():
    """Executa as funções principais do programa"""
    conexao_bd = None
    try:
        conexao_bd = inicializar_banco()
        
        if conexao_bd and conexao_bd.is_connected():
            
            #aqui começa a execução principal do programa
            controlador = BibliotecaController(conexao_bd)
            controlador.run()
        else:
            print("Não foi possível estabelecer a conexão principal com o banco.")

    except mysql.connector.Error as err:
        print(f"Erro: {err}")
    
    finally:
        if conexao_bd and conexao_bd.is_connected():
            conexao_bd.close()

if __name__ == "__main__":
    executar()