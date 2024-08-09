# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]


def zipper(lista1, lista2):
    menor_lista = min(len(lista1), len(lista2))
    return [(lista1[i], lista2[i]) for i in range(menor_lista)] # list comprehension


lista1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
lista2 = ['BA', 'SP', 'MG', 'RJ']
result = zipper(lista1, lista2)

print(result)

# outro jeito (zip)

print(list(zip(lista1, lista2)))

# outro jeito (itertools)

from itertools import zip_longest

print(list(zip_longest(lista1, lista2, fillvalue="Sem Cidade"))) # pega a lista maior