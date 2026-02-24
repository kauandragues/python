from datetime import date

from views.menu_view import MenuView
from models.livro import Livro
from models.usuario import Usuario
from models.emprestimo import Emprestimo

from daos.livro_dao import LivroDAO
from daos.usuario_dao import UsuarioDAO
from daos.emprestimo_dao import EmprestimoDAO

class BibliotecaController:
    
    def __init__(self, conexao_bd):
        self._view = MenuView()
        
        self.livro_dao = LivroDAO(conexao_bd)
        self.usuario_dao = UsuarioDAO(conexao_bd)
        self.emprestimo_dao = EmprestimoDAO(conexao_bd)

        # atualiza o status assim que o programa inicia
        self.atualizar_status_emprestimos_auto()

    # menu principal
    def run(self):
        """Roda o programa principal"""
        while True:
            escolha = self._view.mostrar_menu_principal()
            
            if escolha == '1':
                self.gerenciar_livros()
            elif escolha == '2':
                self.gerenciar_usuarios()
            elif escolha == '3':
                self.gerenciar_emprestimos()
            elif escolha == '0':
                self._view.mostrar_mensagem("Saindo...")
                break
            else:
                self.lidar_com_erro("Opção inválida!")
    
    def atualizar_status_emprestimos_auto(self):
        """Atualizar status sempre que inicia o programa"""
        try:
            afetados = self.emprestimo_dao.atualizar_status_automatico()
        except Exception as e:
            self.lidar_com_erro(f"Erro ao atualizar status de empréstimos: {e}")

    def gerenciar_livros(self):
        """Roda o menu de gerenciamento de livros"""
        while True:
            escolha = self._view.mostrar_menu_livros() 
            if escolha == '1':
                self.cadastrar_livro()
            elif escolha == '2':
                self.listar_livros_separados()
            elif escolha == '3':
                self.buscar_livro_por_titulo()
            elif escolha == '4':
                self.buscar_livro_por_ano()
            elif escolha == '9':
                break
            else:
                self.lidar_com_erro("Opção inválida!")

    def cadastrar_livro(self):
        """Cadastra novos livros"""
        try:
            dados = self._view.obter_dados_livro()

            if dados['titulo'] == "" or dados['autor'] == "" or dados['isbn'] == "" or dados['ano'] == "" or dados['editora'] == "": 
                self.lidar_com_erro("Dados inválidos.")
                return

            if dados['ano'] > 2025:
                self.lidar_com_erro("Ano deve ser menor que 2025'!")
                return

            novo_livro = Livro(
                None, dados['titulo'], dados['autor'],
                dados['isbn'], dados['ano'], dados['editora'],
                'Disponível'
            )
            livro_salvo = self.livro_dao.criar(novo_livro)
            msg = f"Livro '{livro_salvo.titulo}' (ID: {livro_salvo.idLivro}) cadastrado!"
            self._view.mostrar_mensagem(msg)
        except Exception as e:
            self.lidar_com_erro(f"Erro ao cadastrar livro: {e}")

    def listar_livros_separados(self):
        """Lista os livros pelos disponiveis e emprestados"""
        try:
            disponiveis = self.livro_dao.buscar_por_status('Disponível')
            emprestados = self.livro_dao.buscar_por_status('Emprestado')
            self._view.mostrar_livros_separados(disponiveis, emprestados)
        except Exception as e:
            self.lidar_com_erro(f"Erro ao listar livros: {e}")

    def buscar_livro_por_titulo(self):
        """Realiza a busca por titulo"""
        try:
            titulo = self._view.obter_titulo_busca()
            if not titulo:
                return
            resultados = self.livro_dao.buscar_por_titulo_parcial(titulo)
            self._view.listar_livros(resultados, f"Resultados da Busca por Título: '{titulo}'")
        except Exception as e:
            self.lidar_com_erro(f"Erro ao buscar por título: {e}")

    def buscar_livro_por_ano(self):
        """Buscar livros pelo ano de publicação"""
        try:
            ano = self._view.obter_ano_busca()
            if ano is None:
                return
            resultados = self.livro_dao.buscar_por_ano(ano)
            self._view.listar_livros(resultados, f"Resultados da Busca por Ano: {ano}")
        except Exception as e:
            self.lidar_com_erro(f"Erro ao buscar por ano: {e}")

    def gerenciar_usuarios(self):
        """Gerencia o fluxo do menu de usuários"""
        while True:
            escolha = self._view.mostrar_menu_usuarios()
            if escolha == '1':
                self.cadastrar_usuario()
            elif escolha == '2':
                self.listar_usuarios()
            elif escolha == '9':
                break
            else:
                self.lidar_com_erro("Opção inválida!")

    def cadastrar_usuario(self):
        """Cadastrar usuário usando como chave-primária o email"""
        try:
            dados = self._view.obter_dados_usuario()
            if not dados['nome'] or not dados['email']:
                self.lidar_com_erro("Nome e Email não podem ser vazios.")
                return
                
            novo_usuario = Usuario(matriculaUsuario=None, nome=dados['nome'], email=dados['email'])
            usuario_salvo = self.usuario_dao.criar(novo_usuario)
            msg = f"Usuário '{usuario_salvo.nome}' (Matrícula: {usuario_salvo.matriculaUsuario}) cadastrado!"
            self._view.mostrar_mensagem(msg)
        except Exception as e:
            if 'email' in str(e):
                self.lidar_com_erro("Email já cadastrado. Tente outro.")
            else:
                self.lidar_com_erro(f"Erro ao cadastrar usuário: {e}")

    def listar_usuarios(self):
        """Listar usuários da biblioteca"""
        try:
            lista_usuarios = self.usuario_dao.buscar_todos()
            self._view.listar_usuarios(lista_usuarios)
        except Exception as e:
            self.lidar_com_erro(f"Erro ao listar usuários: {e}")

    def gerenciar_emprestimos(self):
        """Gerencia o fluxo do menu de empréstimos"""
        while True:
            escolha = self._view.mostrar_menu_emprestimos()
            if escolha == '1':
                self.realizar_emprestimo()
            elif escolha == '2':
                self.realizar_devolucao()
            elif escolha == '3':
                self.listar_emprestimos_separados()
            elif escolha == '9':
                break
            else:
                self.lidar_com_erro("Opção inválida!")

    def realizar_emprestimo(self):
        """Realiza empréstimos com a matricula do usuário e id do livro"""
        try:
            dados = self._view.obter_dados_emprestimo()
            if not dados:
                return 

            livro = self.livro_dao.buscar_por_id(dados['id_livro'])
            usuario = self.usuario_dao.buscar_por_matricula(dados['matricula_usuario'])

            if not livro or not usuario:
                self.lidar_com_erro("Livro ou Usuário não encontrado.")
                return
            
            if livro.status != 'Disponível':
                self.lidar_com_erro(f"Livro '{livro.titulo}' não está disponível (Status: {livro.status}).")
                return

            novo_emprestimo = Emprestimo(
                None, livro, usuario,
                dados['data_retirada'],
                dados['data_prevista'],
                None,
                'Dentro do Prazo'
            )
            
            self.emprestimo_dao.criar(novo_emprestimo)
            self.livro_dao.atualizar_status(livro, 'Emprestado')
            
            self._view.mostrar_mensagem("Empréstimo realizado com sucesso!")
            
        except Exception as e:
            self.lidar_com_erro(f"Erro ao realizar empréstimo: {e}")

    def realizar_devolucao(self):
        """Realiza devolução de empréstimo"""
        try:
            id_emprestimo = self._view.obter_id_generico("ID do Empréstimo")
            if id_emprestimo is None:
                return

            emprestimo = self.emprestimo_dao.buscar_por_id(id_emprestimo)
            
            if not emprestimo:
                self.lidar_com_erro("Empréstimo não encontrado.")
                return
            
            if emprestimo.dataDevolucaoReal:
                self.lidar_com_erro(f"Este empréstimo já foi devolvido em {emprestimo.dataDevolucaoReal.strftime("%d-%m-%Y")}.")
                return

            print(f"Livro a devolver: {emprestimo.livro.titulo}")
            print(f"Usuário: {emprestimo.usuario.nome}")
            confirmar = input("Confirmar devolução? (S/N): ").strip().lower()
            
            if confirmar != 's':
                self._view.mostrar_mensagem("Devolução cancelada.")
                return

            hoje = date.today()
            emprestimo.dataDevolucaoReal = hoje
            
            # atualiza o status final
            if emprestimo.status != 'Atrasado' and hoje > emprestimo.dataDevolucaoPrevista:
                emprestimo.status = 'Atrasado'
                
            self.emprestimo_dao.atualizar_devolucao(emprestimo)
            self.livro_dao.atualizar_status(emprestimo.livro, 'Disponível')
            
            self._view.mostrar_mensagem(f"Devolução registrada com status: {emprestimo.status}")
            
        except Exception as e:
            self.lidar_com_erro(f"Erro ao realizar devolução: {e}")
        
    def listar_emprestimos_separados(self):
        """Lista emprestimos ativos e devolvidos"""
        try:
            # atualiza status antes de listar
            self.atualizar_status_emprestimos_auto()
            
            ativos = self.emprestimo_dao.buscar_ativos()
            devolvidos = self.emprestimo_dao.buscar_devolvidos()
            self._view.mostrar_emprestimos_separados(ativos, devolvidos)
        except Exception as e:
            self.lidar_com_erro(f"Erro ao listar empréstimos: {e}")
            
    def lidar_com_erro(self, msg: str):
        """Lida com os erros e mostra a excessão"""
        #agora cada mensagem tem o seu texto específico e não precisa ficar reescrevendo o mostrar
        #mensagem
        self._view.mostrar_mensagem(f"ERRO: {msg}")