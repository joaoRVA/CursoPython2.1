"""
Dicionários em Python (tipo dict)

dict e list = dados mutáveis

 Dicionários são estruturas de dados do tipo par de "chave" e "valor".
 Chaves podem ser consideradas como o "índice"
"""


"""

pessoa = dict(nome='João Vítor', sobrenome = 'Rodrigues')
"""
pessoa = {
    'nome': 'João Vítor',
    'Sobrenome': 'Rodrigues',
    'Idade': 20,
    'Altura': 1.75,
    'endereços':[
        {'Rua': 'Monte Líbano', 'Numero': 872},
        {'Rua': 'tam tam', 'Numero': 123},
    ],
}
# print(pessoa, type(pessoa))
print(pessoa['nome'])
print(pessoa['Sobrenome'])
print(pessoa['Idade'])
print(pessoa['Altura'])
print(pessoa['endereços'])
print()


for chave in pessoa:
    print(f'{chave}: {pessoa[chave]}')