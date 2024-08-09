# Introdução à função lambda (função anônima de uma linha)
# A função lambda é uma função como qualquer
# outra em Python. Porém, são funções anônimas
# que contém apenas uma linha. Ou seja, tudo
# deve ser contido dentro de uma única expressão.

# lista = [23, 2, 1, 0, 5,]

# lista.sort(reverse=True)

# sorted(lista) mesma coisa, faz copia rasa
# print(lista)
lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]


# def ordena(item):
#     return item['nome']

# lista.sort(key=ordena) # key determina a função que o python vai usar

# for i in lista:
#     print(i)




# função Lambda

# lista.sort(key=lambda item: item['nome']) # lamda é a palavra pra criar uma função sem nome de uma unica linha

# for i in lista:
#     print(i)




def exibir(list):
    for i in list:
        print(i)
    print()

l1 = sorted(lista, key=lambda item: item['nome']) # pra usar o sorted tem que passar a variavel requerida 'lista'
l2 = sorted(lista, key=lambda item: item['sobrenome'])

exibir(l1)
exibir(l2)