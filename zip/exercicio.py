lista1 = [1, 2, 3, 4, 5, 6, 7]
lista2 = [1, 2, 3, 4]

def zipper(list1, list2):
    zipar = min(len(list1), len(list2))
    return [list1[i] + list2[i] for i in range(zipar)]

print(zipper(lista1, lista2))


print()
# outro jeito
print(list(zip(lista1, lista2)))
soma = [x + y for x, y in zip(lista1, lista2)]

print(soma)