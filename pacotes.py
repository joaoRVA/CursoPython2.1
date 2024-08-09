import sys
# print(*sys.path, sep='\n')
from teste_package.modulo import *


try:
    from teste_package.modulo import soma_numeros_inteiros
except ModuleNotFoundError:
    print("MÓDULO NÃO ENCONTRADO")
print(soma_numeros_inteiros(3, 1))

print(variavel)
# print(subtracao)