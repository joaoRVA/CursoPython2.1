# Objetivo: passar funções normais para lambda

def executa(funcao, *args):
    return funcao(*args)

def soma(x, y):
    return x + y



# 3 exemplos da mesma coisa
print(
    executa(lambda x, y: x + y, 2, 3), # lambda parameter: return, args

        executa(soma, 2, 3),

        soma(2, 3)

)


def cria_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica

multiplica_1 = executa(cria_multiplicador(2), 3)
print(multiplica_1)


multiplica_2 = executa(lambda m: lambda n: n * m, 4)
print(multiplica_2(2))



# da pra usar *args tbm

print(
    
    executa(lambda *args: sum(args), 1, 4, 3, 5, 7)
)