# Generator Expression - são funções que sabem pausar
import sys

lista = [n for n in range(10000)] # a list comprehension salva todos os valores na memória

generator = (n for n in range(10000)) # o generator para no valor em que está, retora um por vez

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

# dito isso, o generator nao tem as mesma funcionalidades da lista por causa disso
#  lista[n] por exemplo


# for i in generator:
#     print(i)