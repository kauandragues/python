# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
import copy

produtos = [
    {"nome": "Produto 5", "preco": 10.00},
    {"nome": "Produto 1", "preco": 22.32},
    {"nome": "Produto 3", "preco": 10.11},
    {"nome": "Produto 2", "preco": 105.87},
    {"nome": "Produto 4", "preco": 69.90},
]

novos_produtos = copy.deepcopy(produtos)
novos_produtos = [{**p, "preco": p["preco"] * 1.1} for p in novos_produtos]
print(novos_produtos)
# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

produtos_ordenados_por_nome = copy.deepcopy(produtos)
produtos_ordenados_por_nome = sorted(
    produtos_ordenados_por_nome, key=lambda p: p["nome"], reverse=True
)
print(produtos_ordenados_por_nome)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
produtos_ordenados_por_preco = copy.deepcopy(produtos)
produtos_ordenados_por_preco = sorted(
    produtos_ordenados_por_preco, key=lambda p: p["preco"]
)
print(produtos_ordenados_por_preco)
