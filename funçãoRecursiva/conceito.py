# Função Recursiva -> é uma função que retorna ela mesma
# Serve para:
    # Resolver problemas grandes em partes menores
# Toda função recursiva deve ter:
    # Um problema que pode ser dividido em partes menores
    # um caso recursivo que resolve o pequeno problema
    # um caso base que para a recursão

def recursiva(inicio=0, fim=10):

    # caso base
    if inicio >= fim:
        return fim
    
    # caso recursivo - conta até chegar ao fim
    inicio += 1
    return recursiva(inicio, fim)

print(recursiva())

# fatorial

def fatorial(n):

    if n <= 1:
        return 1
    return n * fatorial(n - 1)

print(fatorial(5))
print(fatorial(10))

# Se não tiver o caso base pra parar a recursão, o programa vai dar Stack OverFlow
# Isso significa que as callStack's ficaram sobrecarregadas, e o python para qnd chega no limite.