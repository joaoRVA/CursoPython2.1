produtos_origial = [
    {'nome': 'prd 1', 'valor': 20,},
    {'nome': 'prd 2', 'valor': 13,},
    {'nome': 'prd 3', 'valor': 30,},
]


# a lista nova tem que possuir a mesma quantidade de indices da lista original
# isso é mapeamento

novos_produtos = [
    {**produto, 'valor': produto['valor'] * 1.05} # **produto = copia do dicionario pra poder alterar os valores como quiser
    if produto['valor'] > 20 else {**produto} # retorne o dict acima se o valor for maior que 20
    for produto in produtos_origial
]

print(*novos_produtos, sep='\n')