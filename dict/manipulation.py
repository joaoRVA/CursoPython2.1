pessoa = {}

pessoa ['nome'] = 'João Vítor'

print(pessoa)

chave = 'sobrenome'

pessoa[chave] = 'Rodrigues'

print(pessoa[chave])

del pessoa[chave] #deletar chaves

print(pessoa.get('sobrenome')) # retorna None por padrão

if pessoa.get('sobrenome') is None:
    print("bagulho doido")
else:
    print(pessoa[chave])