import mysql.connector

conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="adad",
  database="conta_bancaria"
)
cursor = conn.cursor()

class ContaBancaria:

  def __init__(self, titular, saldo=0.0, conn=None):
    self.titular = titular
    self.__saldo = saldo
    self.conn = conn
    self._criar_tabela()
    self._inserir_conta()

  def _criar_tabela(self):
    cursor = self.conn.cursor()
    cursor.execute("""
      CREATE TABLE IF NOT EXISTS contas (
        titular VARCHAR(50) PRIMARY KEY,
        saldo DECIMAL(10,2)
      ) 
    """)
    self.conn.commit()

  def _inserir_conta(self):
    cursor = self.conn.cursor()
    cursor.execute(
      "INSERT IGNORE INTO contas (titular, saldo) VALUES (%s, %s)",
      (self.titular, self.__saldo)
    )
    self.conn.commit()

  def depositar(self, valor):
    if valor > 0:
      self.__saldo += valor
      cursor = self.conn.cursor()
      cursor.execute(
        "UPDATE contas SET saldo=%s WHERE titular=%s",
        (self.__saldo, self.titular)
      )
      self.conn.commit()

  def get_saldo(self):
    return self.__saldo

class Pessoa:
  def __init__(self, nome, conn):
    self.nome = nome
    self.conn = conn

class Cliente(Pessoa):

  def __init__(self, nome, limite_de_credito, conn):
    super().__init__(nome, conn)
    self.limite_de_credito = limite_de_credito

  def salvar(self):
    cursor = self.conn.cursor()
    cursor.execute("""
      CREATE TABLE IF NOT EXISTS clientes (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(50)
      )
    """)
    cursor.execute("INSERT INTO clientes (nome) VALUES (%s)", (self.nome,))
    self.conn.commit()

  def adicionar_coluna_extra_cliente(self, nome_coluna, tipo_coluna):
    cursor = self.conn.cursor()
    cursor.execute(f"""
      ALTER TABLE cliente
      ADD {nome_coluna} {tipo_coluna};
    """)
    self.conn.commit()

class Pagamento:
  def processar(self):
    raise NotImplementedError
  
class PagamentoCartao(Pagamento):
  def __init__(self, valor, conn):
    self.valor = valor
    self.conn = conn

  def processar(self):
    cursor = self.conn.cursor()
    cursor.execute("""
      CREATE TABLE IF NOT EXISTS pagamentos (
      id INT AUTO_INCREMENT PRIMARY KEY,
      tipo VARCHAR(20),
      valor DECIMAL(10,2))
    """)
  
    cursor.execute("INSERT INTO pagamentos (tipo, valor) VALUES (%s, %s)",
    ("cartao", self.valor))
    self.conn.commit()

conta1 = Cliente("Kauã", 500, conn)
Cliente.adicionar_coluna_extra_cliente(conta1,"limite_de_nao_credito", "INT")
