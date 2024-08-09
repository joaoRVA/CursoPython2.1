"""
Map(): é uma função que aplica uma função a cada elemento de uma lista e retorna uma nova lista com os resultados.
Sintaxe: map(função, lista)


partial(): é uma função que tem como um dos argumentos uma outra funcao, e podemos passar um dos valores parcialmente.
Sintaxe: partial(função, argumentos)
""" 
from functools import partial


produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

def multiplica_por_dois(valor, multiplicador):
    return valor * multiplicador

aumentar_valor = partial(multiplica_por_dois, multiplicador=2)

def muda_preco(product):
    return {**product, 'preco': aumentar_valor(product['preco'])}

teste = list(map(muda_preco, produtos))

print(*teste, sep='\n')