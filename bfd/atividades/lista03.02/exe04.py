"""
Aluno: github/kauandragues

Exercício:Notas Acima da Média 
Objetivo: Calcular e filtrar com base em média. 
Descrição: Após calcular a média de uma lista de notas, imprima quais estão acima. 
Faça dois loops: um para média, outro para filtrar.

"""
notas = []
soma = 0.0
media = 0
qtd_notas = int(input("Digite a quantidade de notas:"))

#armazena notas em lista e acumula as notas na soma
for i in range(qtd_notas):
  nota = float(input("Digite a nota:"))
  notas.append(nota)
  soma += nota

media = soma / qtd_notas #descobre média

#imprimir média e notas acima da média
print(f"\nA média é {media:.2f}")
for nota in notas:
  if nota >= media:
    print(nota)
