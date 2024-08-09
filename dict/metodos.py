# Métodos úteis em dicionários

pessoa = {
    'nome': 'Joca',
    'sobrenome': 'Martins',
}

# print(pessoa.__len__()) retorna o numero de chaves
# print(len(pessoa)) mais usado


# .keys()
print(pessoa.keys()) # retorna as chaves
print(list(pessoa.keys())) # conversão

# .values()
print(tuple(pessoa.values())) # retorna valores

#.items()
print(list(pessoa.items())) # .items() retorna as chaves e os valores

for chaves, valor in pessoa.items():
    print(chaves, valor)

# .setdefault()
pessoa.setdefault('idade', 0) # estabelece um valor padrão a uma chave específica

print(pessoa['idade'])
#.get()
print(pessoa.get('endereco')) # pega o valor, senao tiver nada, retorna None por padrão
print()

# .pop()
ex = {
    'nome2': 'Joao',
    'sobrenome2': 'Rodrigues',
    'telefone': '(19) 99707-2363'
}

nome = ex.pop('nome2') # apaga a chave e retorna a mesma
print(nome)
print(ex)
print()
#.popitem()

ultima_chave = ex.popitem() #remove a ultima chave e retorna a mesma
print(ultima_chave)
print(ex)
print()

# .update() atualiza os valores e chaves

ex.update({
    'nome2': 'Rafael',
    'idade': 20,
})

print(ex)

ex.update(nome3='Bruno', idade2=21)
print(ex)