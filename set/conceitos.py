# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3}
# s1 = set('Luiz')
s1 = set('abner')  # vazio
s2 = {'Luiz', 1, 2, 3}  # com dados

print(type(s1), s1)
print(s2)

# Sets são eficientes para remover valores duplicados de iteráveis.
# - Não aceitam valores mutáveis, como listas;
# - Seus valores serão sempre únicos;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)

s3 = {'gabriela'}
print(s3)
print()

# exemplo

s4 = {1, 2, 5, 4, 3, 5, 6, 4, 3, 2}

s4_convert = list(s4)
print(s4_convert)
print()

# for numero in s4:
#     print(numero)