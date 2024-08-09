# Filter

import pprint

def p(v):
    pprint.pprint(v, sort_dicts= False, width=40)

produtos_origial = [
    {'nome': 'prd 1', 'valor': 20,},
    {'nome': 'prd 2', 'valor': 9,},
    {'nome': 'prd 3', 'valor': 30,},
]


novos_produtos = [
    {**produto, 'valor': produto['valor'] * 1.05}
    if produto['valor'] > 20 else {**produto} 
    for produto in produtos_origial
    if produto['valor'] > 10 # filtro, se o valor do produto for menor que 10, ele nao vai exibir
]
p(novos_produtos)

# p(novos_produtos)

lista = [n for n in range(10) if n < 5] # filter - filtra alguns valores da list comprehension na DIREITA do for

# print(lista)