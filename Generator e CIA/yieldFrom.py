# YieldFrom continua um generator da onde outro parou

#exemplo

def gen1():
    print("começo gen1")
    yield 1
    yield 2
    yield 3
    yield 4
    print('fim gen1')

print()

def gen3():
    print('começo gen3')
    yield 10
    yield 11
    print('fim gen3')

def gen2(gen):
    yield from gen()
    print("começo gen2")
    yield 5
    yield 6
    yield 7
    yield 8
    print('fim gen2')

g = gen2(gen1)
g2 = gen2(gen3)

for n in g:
    print(n)

print()
for n in g2:
    print(n)