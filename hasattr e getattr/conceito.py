# hasattr = serve para verificar se um atributo existe naquela variável

# getattr = é usado para obter o valor de um atributo de um objeto.

string = 'Joao'

metodo = 'upper'

if hasattr(string, metodo):
    print('tem')
    print(getattr(string, metodo)()) # se isso é um metodo entao podemos executar ele com () no final
else:
    print("nao tem")