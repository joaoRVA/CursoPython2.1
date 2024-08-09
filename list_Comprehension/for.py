import pprint

lista = []

for x in range(3):
    for y in range(3):
        lista.append((x, y))

# como fazer o mesmo em list comprehension

lista = [
    (x, y) 
    for x in range(3)
    for y in range(3)
]

pprint.pprint(lista, sort_dicts=False, width=70)