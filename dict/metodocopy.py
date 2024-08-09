import copy

"""
copy

shallow copy = copia rasa
copia as chaves e os valores de uma forma rasa

"""

d1 = {
    'nome': 'joao',
    'idade': 10,
    'li': [0, 1, 2],
}

d2 = d1 

d2['idade'] = 20 # dessa forma os dois mudam, pq são a mesma coisa
print(d1)
print(d2) 
print()

# por isso que existe o método copy

d2 = d1.copy() # copia os valores do d1 para o d2

d2['idade'] = 1000
print(d2)
print(d1)
print()

# porém, quando temos dados mutáveis dentro do dicionário, isso acontece:

d2['li'][1] = 500 # o copy() não copia os dados mais aprofundamente, como os valores da lista
print(d2)
print(d1)
print()

# para isso, o python tem o módulo chamado copy que faz a deepcopy

d3 = {
    'list': [0, 1, 2, 3],
}

d4 = copy.deepcopy(d3) # Use deepcopy para copiar profundamente
d4['list'][2] = 'Mudei'
print(d3)
print(d4)
