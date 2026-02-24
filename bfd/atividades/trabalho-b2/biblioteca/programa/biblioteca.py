# ------------------------------------------------------------------#
# Sistema de Biblioteca
# Autor: Kauã de Andrade Rodrigues
# Data Criação: 10/08/2025
# Data Última Atualização: 27/08/2025
# Atualização Feita por: Kauã de Andrade Rodrigues
# Versão: 1.0
# Principais Funções: carregar_dados(), salvar_dados(),
# cadastrar_livro(), cadastrar_usuario(),
# registrar_emprestimo(), registrar_devolucao(), buscar_livro_por_ano(),
# buscar_livro_por_titulo(), listar_livros_disponiveis(), listar_emprestimos(),
# atualizar_status_emprestimo()
# ------------------------------------------------------------------#
# Importações necessárias
import csv
from datetime import datetime, timedelta
# Estruturas de dados (listas)
livros = []
usuarios = []
emprestimos = []

# -----------------------------
# Funções principais
# -----------------------------


def carregar_dados():
    # -----------------------------
    # Carrega dados de arquivos CSV (livros, usuários, empréstimos, editoras e autores).
    # -----------------------------

    # Carrega dados para livros
    try:
        with open("livros.csv", "r", newline="") as arquivo_livro:
            leitor_csv = csv.reader(arquivo_livro)
            next(leitor_csv)  # pula o cabeçalho
            for linha in leitor_csv:
                livros.append(linha)
    except FileNotFoundError:
        print("Arquivo de livros.csv não encontrado :(")
        return

    # Carrega dados para usuários
    try:
        with open("usuarios.csv", "r", newline="") as arquivo_usuario:
            leitor_csv = csv.reader(arquivo_usuario)
            next(leitor_csv)  # pula o cabeçalho
            for linha in leitor_csv:
                usuarios.append(linha)
    except FileNotFoundError:
        print("Arquivo de usuarios.csv não encontrado :(")
        return

    # Carrega dados para empréstimos
    try:
        with open("emprestimos.csv", "r", newline="") as arquivo_emprestimos:
            leitor_csv = csv.reader(arquivo_emprestimos)
            next(leitor_csv)  # pula o cabeçalho
            for linha in leitor_csv:
                emprestimos.append(linha)
    except FileNotFoundError:
        print("Arquivo de emprestimos.csv não encontrado :(")
        return

    # Atualiza os emprestimo com atrasado ou dentro do prazo
    atualizar_status_emprestimo()


def salvar_dados():
    # -----------------------------
    # Salva dados em arquivos CSV.
    # -----------------------------

    # salvar lista de livros no arquivo csv
    try:
        with open("livros.csv", "w", newline="") as arquivo_livros:
            escritor = csv.writer(arquivo_livros)
            escritor.writerow(["idLivro", "titulo", "ISBN", "ano",
                              "nomeEditora", "nomeAutor", "status"])  # cabeçalho
            escritor.writerows(livros)
    except Exception as e:
        print(f"Erro ao salvar dados dos livros no arqiuvo csv :(\n{e}")
        return

    try:
        with open("usuarios.csv", "w", newline="") as arquivo_usuarios:
            escritor = csv.writer(arquivo_usuarios)
            escritor.writerow(
                ["matriculaUsuario", "nome", "email"])  # cabeçalho
            escritor.writerows(usuarios)
    except Exception as e:
        print(f"Erro ao salvar dados dos livros no arqiuvo csv :(\n{e}")
        return

    try:
        with open("emprestimos.csv", "w", newline="") as arquivo_emprestimos:
            escritor = csv.writer(arquivo_emprestimos)
            escritor.writerow(["idEmprestimo", "dataRetirada", "dataDevolucaoPrevista",
                              "dataDevolucaoReal", "status", "idLivro", "matriculaUsuario"])  # cabeçalho
            escritor.writerows(emprestimos)
    except Exception as e:
        print(f"Erro ao salvar dados dos livros no arqiuvo csv :(\n{e}")
        return


def cadastrar_livro():
    # -----------------------------
    # Solicita informações do livro e adiciona à lista 'livros'.
    # -----------------------------
    titulo = input("Digite o título do livro:")

    try:
        isbn = int(input("Digite o isbn do livro (digite apenas números):"))
    except ValueError:  # validar tipo da entrada
        print("Você não digitou apenas números :(")
        return

    try:
        ano = int(input("Digite o ano do livro (digite um número inteiro):"))
    except ValueError:  # validar tipo da entrada
        print("Você não digitou um número inteiro :(")
        return

    editora = input("Digite o nome da editora do livro:")
    autor = input("Digite o nome do(a) autor(a) do livro:")
    status = "Disponível"

    # id autoincremetal, cria uma registro novo de livro
    novo_livro = [len(livros)+1, titulo, isbn, ano, editora, autor, status]
    livros.append(novo_livro)  # adiciona o livro na lista de livros
    print("Livro cadastrado com sucesso!")


def cadastrar_usuario():
    # -----------------------------
    # Solicita informações do usuário e adiciona à lista 'usuarios'.
    # -----------------------------

    nome = input("Digite o nome do usuário:")
    email = input("Digite o email do usuário:")

    for usuario in usuarios:
        if usuario[2] == email:
            print("Esse email já está cadastrado! Tente novamente.")
            return

    # matricula autoincremetal, cria uma registro novo de usuário
    novo_usuario = [len(usuarios)+1, nome, email]
    usuarios.append(novo_usuario)  # adiciona o usuário na lista de usuários
    print("Usuário cadastrado com sucesso!")


def registrar_emprestimo():
    # -----------------------------
    # Registra um novo empréstimo, alterando status do livro.
    # -----------------------------

    data_retirada = datetime.now().date()  # pegar o dia de hoje
    data_devolucao = data_retirada + \
        timedelta(days=7)  # somar 7 dias no dia de hoje

    data_retirada_string = data_retirada.strftime(
        "%d-%m-%Y")  # transformar em string
    data_devolucao_string = data_devolucao.strftime(
        "%d-%m-%Y")  # transformar em string

    data_devolucao_real = ""  # será preenchido no registrar devolução

    status = "Dentro do Prazo"  # sempre começa dentro de prazo
    try:
        id_livro = int(input("Digite o id do livro:"))
    except ValueError:  # validar tipo da entrada
        print("Você não digitou apenas números :(")
        return

    # validar se livro existe

    livro_existe = False
    for livro in livros:
        if int(livro[0]) == id_livro:
            livro_existe = True

    if livro_existe is False:
        print("O id de livro digitado não existe!")
        return

    # validar se livro já foi emprestado
    for livro in livros:
        if int(livro[0]) == id_livro and livro[6] != "Disponível":
            print("Esse livro já está emprestado, tente outro!")
            return

    try:
        matricula_usuario = int(input("Digite a matricula do usuário:"))
    except ValueError:  # validar tipo da entrada
        print("Você não digitou um número inteiro :(")
        return

    # validar se o usuário existe
    existe_usuario = False
    for usuario in usuarios:
        if int(usuario[0]) == matricula_usuario:
            existe_usuario = True

    if existe_usuario is False:
        print("Esse usuário não existe!")
        return

    novo_emprestimo = [len(emprestimos)+1, data_retirada_string, data_devolucao_string, data_devolucao_real,
                       # id autoincremetal, cria uma registro novo de emprestimo
                       status, id_livro, matricula_usuario]
    emprestimos.append(novo_emprestimo)  # adiciona o livro na lista de livros

    # atualizar status do livro
    for livro in livros:
        if int(livro[0]) == id_livro:
            livro[6] = "Emprestado"

    print("Emprestimo realizado com sucesso!")


def registrar_devolucao():
    # -----------------------------
    # Atualiza status do livro como devolvido.
    # -----------------------------
    try:
        id_emprestimo = int(
            input("Digite o id do emprestimo (digite um número inteiro):"))
    except ValueError:
        print("Você não digitou um número inteiro!")
    existe_id_emprestimo = False

    # verifica se existe esse id de emprestimo
    for emprestimo in emprestimos:
        if int(emprestimo[0]) == id_emprestimo:
            existe_id_emprestimo = True
            break

    if existe_id_emprestimo is not True:
        print("O id de emprestimo digitado não existe!")
        return

    # verifica se o emprestimo é devolvivel
    for emprestimo in emprestimos:
        if int(emprestimo[0]) == id_emprestimo and emprestimo[3] != '':
            print("Esse emprestimo já foi devolvido!")
            return

    # pega o id digitado, busca o nome do livro e diz quem foi o usuário que emprestado
    # depois verifica se o usuário deseja realmente continuar com a devolução
    # pega a lista de emprestimo do mais recente primeiro
    for emprestimo in emprestimos[::-1]:
        if int(emprestimo[0]) == id_emprestimo and emprestimo[3] == '':

            for livro in livros:
                # pega o titulo do livro emprestado
                if int(emprestimo[5]) == int(livro[0]):
                    print(f"O livro a ser devolvido é {livro[1]}")

            for usuario in usuarios:
                # mostra as informações do usuário que emprestou o livro
                if int(emprestimo[6]) == int(usuario[0]):
                    print(f"A matricula do usuário é {usuario[0]}")
                    print(f"O nome do usuário é {usuario[1]}")

            prosseguir = input(
                "\nDeseja prosseguir? Digite (S) para sim e qualquer outro caracter para não:")
            if prosseguir.lower() == "s":
                data_devolucao_real = datetime.now().date().strftime("%d-%m-%Y")
                emprestimo[3] = data_devolucao_real

                # altera a disponibilidade do livro
                for livro in livros:
                    if int(emprestimo[5]) == int(livro[0]):
                        livro[6] = "Disponível"

                print("Devolução do emprestimo realizada com sucesso!")
                return


def listar_livros_disponiveis():
    # -----------------------------
    # Exibe todos os livros com status 'disponível' e não disponíveis.
    # -----------------------------

    if len(livros) == 0:
        print("Não há nenhum livro cadastrado!")
        return

    print("\nLista de Livros Disponíveis")
    print(f"{"ID":3} | {"Título":20} | {"ISBN":20} | {"Ano":4} | {"Editora":20} | {"Autor":20}")
    print("-----------------------------------------------------------------------------------------------------")
    for livro in livros:
        if livro[6] == "Disponível":
            print(
                f"{livro[0]:<3} | {livro[1]:<20} | {livro[2]:<20} | {livro[3]:<4} | {livro[4]:<20} | {livro[5]:<20}")
    print("-----------------------------------------------------------------------------------------------------")

    print("\nLista de Livros Emprestados")
    print(f"{"ID":3} | {"Título":20} | {"ISBN":20} | {"Ano":4} | {"Editora":20} | {"Autor":20}")
    print("-----------------------------------------------------------------------------------------------------")
    for livro in livros:
        if livro[6] == "Emprestado":
            print(
                f"{livro[0]:<3} | {livro[1]:<20} | {livro[2]:<20} | {livro[3]:<4} | {livro[4]:<20} | {livro[5]:<20}")
    print("-----------------------------------------------------------------------------------------------------")


def listar_emprestimos():
    # -----------------------------
    # Mostra todos os empréstimos ativos ou históricos.
    # -----------------------------
    if len(emprestimos) == 0:
        print("Nenhum emprestimo foi realizado!")
        return

    print("\nLista de Empréstimos Ativos")
    print(f"{"ID":3} | {"Retirada":10} | {"Previsão":10} | {"Status":15} | {"ID Livro":9} | {"Título:":20} | {"Matricula:":15} | {"Nome":15}")
    print("--------------------------------------------------------------------------------------------------------------------------------")
    for emprestimo in emprestimos:
        if emprestimo[3] == '':
            for livro in livros:
                if int(livro[0]) == int(emprestimo[5]):
                    for usuario in usuarios:
                        if int(usuario[0]) == int(emprestimo[6]):
                            print(
                                f"{emprestimo[0]:<3} | {emprestimo[1]:<10} | {emprestimo[2]:<10} | {emprestimo[4]:<15} | {emprestimo[5]:<9} | {livro[1]:<20} | {emprestimo[6]:<15} | {usuario[1]:<15}")
    print("--------------------------------------------------------------------------------------------------------------------------------")

    print("\nLista de Empréstimos Já Devolvidos")
    print(f"{"ID":3} | {"Retirada":10} | {"Previsão":10} | {"Devolução":10} | {"Status":15} | {"ID Livro":9} | {"Título:":20} | {"Matricula:":15} | {"Nome:":15}")
    print("---------------------------------------------------------------------------------------------------------------------------------")
    for emprestimo in emprestimos:
        if emprestimo[3] != '':
            for livro in livros:
                if int(livro[0]) == int(emprestimo[5]):
                    for usuario in usuarios:
                        if int(usuario[0]) == int(emprestimo[6]):
                            print(
                                f"{emprestimo[0]:<3} | {emprestimo[1]:<10} | {emprestimo[2]:<10} | {emprestimo[3]:<10} | {emprestimo[4]:<15} | {emprestimo[5]:<9} | {livro[1]:<20} | {emprestimo[6]:<15} | {usuario[1]:<15}")
    print("--------------------------------------------------------------------------------------------------------------------------------")


def atualizar_status_emprestimo():
    # -----------------------------
    # Atualiza o status do emprestimo com a data atual
    # -----------------------------
    data_hoje = datetime.now().date()
    for emprestimo in emprestimos:
        if emprestimo[3] != '':
            continue
        data_prevista = emprestimo[2]
        data_prevista_date = datetime.strptime(
            data_prevista, "%d-%m-%Y").date()

        # verifica se hoje já passou da previsão de entrega do empréstimo
        if data_hoje > data_prevista_date:
            emprestimo[4] = "Atrasado"
        else:
            emprestimo[4] = "Dentro do prazo"


def buscar_livro_por_ano():
    # -----------------------------
    # Buscar livros por ano
    # -----------------------------
    try:
        busca_ano_livro = int(
            input("Digite o ano do livro (digite um número inteiro):"))
    except ValueError:
        print("Você não digitou um número inteiro!")
        return

    # valida para saber se há pelo menos 1 livro com esse ano
    existe_livro = False
    for livro in livros:
        if int(livro[3]) == busca_ano_livro:
            existe_livro = True

    if existe_livro is False:
        print("Não existe nenhum livro com esse ano!")
        return

    print(f"{"ID":3} | {"Título":20} | {"ISBN":20} | {"Ano":4} | {"Editora":20} | {"Autor":20} | {"Status":10}")
    print("---------------------------------------------------------------------------------------------------------------")
    for livro in livros:
        if int(livro[3]) == busca_ano_livro:
            print(
                f"{livro[0]:<3} | {livro[1]:<20} | {livro[2]:<20} | {livro[3]:<4} | {livro[4]:<20} | {livro[5]:<20} | {livro[6]:<10}")
    print("---------------------------------------------------------------------------------------------------------------")


def buscar_livro_por_titulo():
    # -----------------------------
    # Busca livros por título
    # -----------------------------
    try:
        busca_titulo_livro = input("Digite o título do livro:")
    except ValueError:
        print("Você não digitou um número inteiro!")
        return

    # valida para saber se há pelo menos 1 livro com esse título
    existe_livro = False
    for livro in livros:
        if livro[1].lower() == busca_titulo_livro.lower():
            existe_livro = True

    if existe_livro is False:
        print("Não existe nenhum livro com esse título!")
        return

    print(f"{"ID":3} | {"Título":20} | {"ISBN":20} | {"Ano":4} | {"Editora":20} | {"Autor":20} | {"Status":10}")
    print("---------------------------------------------------------------------------------------------------------------")
    for livro in livros:
        if livro[1].lower() == busca_titulo_livro.lower():
            print(
                f"{livro[0]:<3} | {livro[1]:<20} | {livro[2]:<20} | {livro[3]:<4} | {livro[4]:<20} | {livro[5]:<20} | {livro[6]:<10}")
    print("---------------------------------------------------------------------------------------------------------------")

# -----------------------------
# Menu principal
# -----------------------------


def menu():
    while True:
        print("\n=== Sistema de Biblioteca ===")
        print("1 - Cadastrar Livro")
        print("2 - Cadastrar Usuário")
        print("3 - Registrar Empréstimo")
        print("4 - Registrar Devolução")
        print("5 - Listar Livros Disponíveis")
        print("6 - Listar Empréstimos")
        print("7 - Buscar Livro por Ano")
        print("8 - Buscar Livro por Título")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            cadastrar_livro()
        elif opcao == "2":
            cadastrar_usuario()
        elif opcao == "3":
            registrar_emprestimo()
        elif opcao == "4":
            registrar_devolucao()
        elif opcao == "5":
            listar_livros_disponiveis()
        elif opcao == "6":
            listar_emprestimos()
        elif opcao == "7":
            buscar_livro_por_ano()
        elif opcao == "8":
            buscar_livro_por_titulo()
        elif opcao == "0":
            salvar_dados()
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.")


# -- ---------------------------
# Execução principal
# -----------------------------
carregar_dados()
menu()
