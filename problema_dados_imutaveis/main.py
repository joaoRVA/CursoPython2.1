# Problemas de dados imutáveis como parâmetros em funções

def cria_lista(valor, lista=[]):
    lista.append(valor)
    return lista


cliente1 = cria_lista(1000)
cria_lista(300, cliente1)
print(cliente1)

cliente2 = cria_lista('lista2')
cria_lista(200, cliente2)
print(cliente2) # perceba que o python não cria uma nova lista, ele utiliza a mesma.


# Uma das maneiras de se corrigir isso é colocar o valor padrão como None
# e dps transformar em uma lista com if
def nova_lista(valor, lista=None):
    if lista is None:
        lista = []

    lista.append(valor)
    return lista

cliente3 = nova_lista(400)
nova_lista(500, cliente3)
print(cliente3)

cliente4 = nova_lista(600)
nova_lista(800, cliente4)
print(cliente4) # Perceba que aqui gerou uma nova lista