# variável livre - nonlocal (locals, globals)

def fora(x):
    a = x
    def dentro(b):
        # print(locals())
        nonlocal a # agora o python entende que esta freevar não é local
        a += b
        return a
    return dentro


valor = fora(1)

# print(valor(2))
# print(valor(4))



def concatenar(string_inicial):
    valor_final = string_inicial

    def interna(valor_a_concatenar=''):
        nonlocal valor_final
        valor_final += valor_a_concatenar
        return valor_final
    return interna

concat = concatenar('a')

print(concat('b'))
print(concat('c'))
print(concat('d'))

final = concat()
print(final)
