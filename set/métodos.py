# metodos uteis

s1 = set()

# .add() adiciona um elemento, só aceita um item por vez
s1.add('JOAO')
s1.add(1)
print(s1)

# .update() adiciona elementos iteráveis, mais de um
print()
# s1.update('vinicius', '1', '3')
# print(s1)

s1.update(('vinicius', 1, 3)) #uma forma de não imprimir as iterações das strings 
print(s1)

# s1.clear() limpa o set

# .discard() elimina um valor especificado
s1.discard('JOAO')
print(s1)