from datetime import date, timedelta
from models.livro import Livro
from models.usuario import Usuario
from models.emprestimo import Emprestimo

class MenuView:
    
    def mostrar_menu_principal(self) -> str:
        """Mostra o menu principal da biblioteca"""
        print("\n--------- Menu Principal da Biblioteca ---------")
        print("1. Gerenciar Livros")
        print("2. Gerenciar Usuários")
        print("3. Gerenciar Empréstimos")
        print("0. Sair")
        return input("Digite sua opção: ").strip()

    def mostrar_mensagem(self, msg: str):
        """Mostra mensagens específicas"""
        print(f"\n{msg}\n")

    def obter_id_generico(self, tipo_id: str) -> int | None:
        """Pede ao usuário um id genérico"""
        #preciso ficar pedindo o id várias vezes, DRY!
        try:
            id_str = input(f"Digite o {tipo_id}: ").strip()
            return int(id_str)
        except ValueError:
            self.mostrar_mensagem("ID inválido. Deve ser um número.")
            return 

    # Menus de Livro
    
    def mostrar_menu_livros(self) -> str:
        """Mostra o menu de livros"""
        print("\n--------- Gerenciar Livros ---------")
        print("1. Cadastrar novo livro")
        print("2. Listar livros (Separados por Status)")
        print("3. Buscar livro por Título")
        print("4. Buscar livro por Ano")
        print("9. Voltar ao menu principal")
        return input("Digite sua opção: ").strip()

    def obter_dados_livro(self) -> dict:
        """Pede ao usuário os dados de um livro para cadastro"""
        print("\n--------- Cadastro de Novo Livro ---------")
        titulo = input("Título: ")
        autor = input("Autor: ")

        try:
            isbn = int(input("ISBN: ")) 
        except ValueError:
            self.mostrar_mensagem("ISBN deve ser um número!")
            isbn = ""

        try:
            ano = int(input("Ano de Publicação: "))
        except ValueError:
            self.mostrar_mensagem("Ano deve ser um número!")
            ano = ""

        editora = input("Editora: ")

        return {
            "titulo": titulo, "autor": autor, "isbn": isbn,
            "ano": ano, "editora": editora
        }

    def listar_livros(self, livros: list[Livro], titulo_secao: str = "Lista de Livros"):
        """Listar qualquer livro lista de livro."""
        print(f"\n--------- {titulo_secao} ---------")
        if not livros:
            print(f"Nenhum livro encontrado para esta seleção.")
            return
        
        print(f"{'ID':<4} | {'Título':<30} | {'ISBN':<13} | {'Ano':<5} | {'Editora':<20} | {'Autor':<25} | {'Status':<12}")
        print("-" * 118) 
        for livro in livros:
            print(f"{livro.idLivro:<4} | {livro.titulo:<30} | {livro.ISBN:<13} | {livro.ano:<5} | {livro.nomeEditora:<20} | {livro.nomeAutor:<25} | {livro.status:<12}")

    def mostrar_livros_separados(self, disponiveis: list[Livro], emprestados: list[Livro]):
        """Mostrar livros separados por status"""
        self.listar_livros(disponiveis, "Livros Disponíveis")
        print("\n")
        self.listar_livros(emprestados, "Livros Emprestados")

    def obter_titulo_busca(self) -> str:
        """Pede ao usuário o título ou parte dele para realizar a busca por título"""
        return input("Digite o Título (ou parte dele) para buscar: ").strip()
        
    def obter_ano_busca(self) -> int | None:
        """Pede ao usuário o ano para realizar a busca por ano"""
        try:
            ano_str = input("Digite o Ano de publicação para buscar: ").strip()
            return int(ano_str)
        except ValueError:
            self.mostrar_mensagem("Ano inválido. Deve ser um número.")
            return None

    # Menus de Usuário
    
    def mostrar_menu_usuarios(self) -> str:
        """Mostra o menu para o gerenciamento de usuário"""
        print("\n--------- Gerenciar Usuários ---------")
        print("1. Cadastrar novo usuário")
        print("2. Listar todos os usuários")
        print("9. Voltar ao menu principal")
        return input("Digite sua opção: ").strip()

    def obter_dados_usuario(self) -> dict:
        """Pede ao usuário os dados para cadastrar um usuário"""
        print("\n--------- Cadastro de Novo Usuário---------")
        nome = input("Nome: ")
        email = input("Email: ")
        return {"nome": nome, "email": email}

    def listar_usuarios(self, usuarios: list[Usuario]):
        """Lista os usuários"""
        print("\n--------- Lista de Usuários ---------")
        if not usuarios:
            print("Nenhum usuário cadastrado.")
            return
        
        print(f"{'Matrícula':<10} | {'Nome':<30} | {'Email':<30}")
        print("-" * 75)
        for usuario in usuarios:
            print(f"{usuario.matriculaUsuario:<10} | {usuario.nome:<30} | {usuario.email:<30}")

    # Menus de Empréstimo
    
    def mostrar_menu_emprestimos(self) -> str:
        """Mostra o menu para o gerenciamento de empréstimo"""
        print("\n--------- Gerenciar Empréstimos ---------")
        print("1. Realizar novo empréstimo")
        print("2. Realizar devolução")
        print("3. Listar empréstimos (Ativos / Devolvidos)")
        print("9. Voltar ao menu principal")
        return input("Digite sua opção: ").strip()

    def obter_dados_emprestimo(self) -> dict | None:
        """Pede ao usuário os dados dos empréstimos"""
        print("\n--------- Novo Empréstimo ---------")
        try:
            id_livro = int(input("ID do Livro: "))
            matricula_usuario = int(input("Matrícula do Usuário: "))
            
            hoje = date.today()
            data_prevista = hoje + timedelta(days=7)
            
            return {
                "id_livro": id_livro, "matricula_usuario": matricula_usuario,
                "data_retirada": hoje, "data_prevista": data_prevista
            }
        except ValueError:
            self.mostrar_mensagem("ID inválidos. Use apenas números.")
            return None

    def listar_emprestimos(self, emprestimos: list[Emprestimo], titulo_secao: str):
        """Listar qualquer lista de empréstimos."""
        print(f"\n--------- {titulo_secao} ---------")
        if not emprestimos:
            print(f"Nenhum empréstimo encontrado para esta seleção.")
            return
            
        for emp in emprestimos:
            if emp.dataDevolucaoReal:
                devolucao = emp.dataDevolucaoReal.strftime("%d/%m/%Y")
            else:
                devolucao = "Pendente"

            retirada_fmt = emp.dataRetirada.strftime("%d/%m/%Y")
            prevista_fmt = emp.dataDevolucaoPrevista.strftime("%d/%m/%Y")

            print(f"ID Empréstimo: {emp.idEmprestimo} | Status: {emp.status}")
            print(f"  - Livro:   {emp.livro.titulo} (ID: {emp.livro.idLivro})")
            print(f"  - Usuário: {emp.usuario.nome} (Matricula: {emp.usuario.matriculaUsuario})")
            print(f"  - Datas: Retirada: {retirada_fmt} | Prevista: {prevista_fmt} | Devolução: {devolucao}\n")

    def mostrar_emprestimos_separados(self, ativos: list[Emprestimo], devolvidos: list[Emprestimo]):
        """Mostrar empréstimos separados por status"""
        self.listar_emprestimos(ativos, "Empréstimos Ativos")
        print("\n" + "="*75 + "\n")
        self.listar_emprestimos(devolvidos, "Empréstimos Devolvidos")