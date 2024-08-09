# Iterator - tem a unica função de entregar o próximo valor do Iterable

iterable = ['Eu', 'Tenho', '__Iter__']

iterator = iter(iterable) # o iterator CONTÉM __iter__ e next()

print(next(iterator))
print(next(iterator))
print(next(iterator))
# print(next(iterator)) quando o iterator passa do numero de indices do iterable, é dado como StopInteration
# O For trata o StopInteration e pausa o laço