# Filter - filtra os dados de um iterável através de uma função.
# Da pra fazer com list comprehension também, mas o python tem esse bagulho pra facilitar
# programação funcional
# Sintaxe: filter(função, iterável)


produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# com list comprehension

novos_produtos = [
    p for p in produtos
    if p['preco'] > 40
]

print(*produtos, sep="\n")
print()
print(*novos_produtos, sep="\n")
print()

# com Filter

def filtrar(param):
    if param['preco'] > 40:
        return param['preco']

# exemplo 1
new_products = filter(lambda p: p['preco'] > 40, produtos)

print(*new_products, sep="\n")
print()

# exemplo 2
new_products_2 = filter(filtrar, produtos)
print(*new_products_2, sep="\n")