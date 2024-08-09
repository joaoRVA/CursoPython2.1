# empacotamento e desempacotamento de dicionários

# a, b = 1, 2
# a, b = b, a
# print(a, b)

# pessoa = {
#     'nome': 'Joao',
#     'sobrenome': 'Rodrigues',
# }

# (a1, a2), (b1, b2) = pessoa.items()

# print(a1, a2)
# print(b1, b2)

# for chave, valor in pessoa.items():
#     print(chave, valor)

pessoa = {
    'nome': 'Joao',
    'sobrenome': 'Rodrigues',
}

dados_pessoa = {
    'idade': 20,
    'altura': 1.75,
}


#Como juntar esses dois dicionários

# criar um dicionário e colocar a extração de outro dict dentro
pessoa_completa = {
    **pessoa,
    **dados_pessoa,
    
 } 

print(pessoa_completa)


# args = argumentos não nomeados

# kwargs = keyword arguments (argumentos nomeados) 
# as kwargs retornam os valores em dicionários


def mostra_argumentos_nomeados(*args, **kwargs):
    print(args, "Não Nomeados")

    for chave, valor in kwargs.items():
        print(chave, valor)

mostra_argumentos_nomeados(1, 2, 3, nome='Jhonny', idade='16',)



# serve para desempacotar tbm

configuracoes = {
    'conf1': 1,
    'conf2': 2,
    'conf3': 3,
    'conf4': 4,
}

mostra_argumentos_nomeados(**configuracoes)