# Set Comprehension & Dict Comprehension

produto = {
    'nome': 'Tênis',
    'preco': 17.90,
    'categoria': 'Roupas',
}

# dict

novo_produto = {
    chave: valor.upper() # se for string vai ficar com letras maiúsculas
    if isinstance(valor, str) else valor # isinstance() checa se o valor é de algum tipo
    for chave, valor in produto.items()
}

print(novo_produto)


# set


st = {n for n in range(10)}

print(st)