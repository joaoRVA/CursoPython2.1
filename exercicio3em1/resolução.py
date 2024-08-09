import copy
from produtos_import import produtos

novos_produtos = [
    
    
    {**p, 'preco': round(p['preco']*1.1, 2)}
    for p in copy.deepcopy(produtos)
]


# print(*produtos, sep='\n')
# print()
# print(*novos_produtos, sep='\n')
# print()

        

produtos_ordenados_por_preco = sorted(copy.deepcopy(novos_produtos), key=lambda item: item['preco'])

produtos_ordenados_por_nome = sorted(copy.deepcopy(novos_produtos), key=lambda item: item['nome'], reverse=True)
print('Produtos ordenados por preço: \n',
    *produtos_ordenados_por_preco, sep='\n'
)
print()
print('produtos ordenados por nome: \n',
    *produtos_ordenados_por_nome, sep='\n'
)