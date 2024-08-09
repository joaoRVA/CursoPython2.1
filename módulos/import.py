# Módulos padrão do Python (import, from, as e *)
# https://docs.python.org/3/py-modindex.html
# inteiro - import nome_modulo
# Vantagens: você tem o namespace do módulo
# Desvantagens: nomes grandes

# import sys

# print(sys.platform)


# partes - from nome_modulo import objeto1, objeto2
# Vantagens: nomes pequenos
# Desvantagens: Sem o namespace do módulo

# from sys import exit, platform

# print('oi', platform)
# exit()
# print('tchau')

# import modulo as nome_apelido

# import sys as s

# s.exit()

# from sys import exit as e, platform as p

# e()
# print(p)

# má prática - from nome_modulo import *
# Vantagens: importa tudo de um módulo
# Desvantagens: importa tudo de um módulo
from sys import *

print(platform)