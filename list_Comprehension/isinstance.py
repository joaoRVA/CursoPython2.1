lista = [
    123, 12.3, 'alou', {1, 2},
    True, (0, 1, 2,), {'nome': 'Joao'},
]


for item in lista:
    if isinstance(item, set):
        print('SET')
        print(item, isinstance(item, set))

    elif isinstance(item, str):
        print('STR')
        print(item.upper())

    elif isinstance(item, (int, float)):
        print('NUM')
        print(item)
    else:
        print('Outro')
        print(item)