# reduce - faz a redução de um iterável em um unico valor
# Sintaxe: reduce(função, iterável, valor inicial)

from functools import reduce

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# método tradicional

inicial = 0

for p in produtos:
    inicial += p['preco']
print(inicial)

# função sum() com list comprehension
print(sum([p['preco'] for p in produtos]))

# reduce
# o acumulador salva o valor da ultima iteração, então podemos soma-lo com o valor do produto atual
# até atingir o final da iteração

def funcao_do_reduce(acumulador, produto):
    print("acumulador: ", acumulador)
    print("produto: ", produto)
    print()
    return acumulador + produto['preco']

reduzir = reduce(funcao_do_reduce, produtos, 0)

print(reduzir)