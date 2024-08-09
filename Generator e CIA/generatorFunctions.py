def generator(n=0):
    yield 1 # Pause
    print('Continuando...')
    yield 2 # Pause
    print('Voltando...')
    yield 3
    print("mais uma vez...")
    return 'Pediu pra parar, PAROU'

gen = generator(n=0)

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
# for n in gen:
#     print(n)