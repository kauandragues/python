'''
alias -> apelido
inner join
left join
right join
 
'''
import mysql.connector

conn = mysql.connector.connect(
host='localhost', user='root',
password='andreiak01', database='mydb')
cursor = conn.cursor()
#cursor.execute('SELECT a.id, a.nome, a.idade, a.id_turma FROM aluno a LEFT JOIN turma t ON a.id_turma = t.id WHERE t.id IS NULL')
#cursor.execute('SELECT AVG(a.idade), t.nome_turma FROM aluno a INNER JOIN turma t ON t.id = a.id_turma GROUP BY id_turma')
#cursor.execute('SELECT t.nome_turma, COUNT(*) from aluno a JOIN turma t ON a.id_turma = t.id GROUP BY id_turma HAVING COUNT(*) > 3')
#cursor.execute('SELECT * FROM aluno ORDER BY idade DESC')
#cursor.execute('SELECT * FROM aluno ORDER BY nome ASC')

'''
Escreva um código em Python que receba uma idade
mínima e liste os alunos com idade maior ou igual a esse
valor
'''

idade_minima = int(input("Digite a idade mínima:"))
cursor.execute(f'SELECT * FROM aluno WHERE idade >= {idade_minima}')
for row in list(cursor.fetchall()):
  print(row)