# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover/ Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.
# Decoradores são "Syntax Sugar" (Açúcar sintático)

def decora_funcao(func):
    def interna(*args, **kwargs):
        for arg in args:
            is_string(arg)
        resultado = func(*args, **kwargs)
        return resultado
    return interna

@decora_funcao # syntax Sugar
def inverte(string):
    print(inverte.__name__) # essa funcao agora passa a ser a outra
    return string[::-1]


def is_string(param):
    if not isinstance(param, str):
        raise TypeError("Esse valor não é aceito, somente strings.")

inverter = inverte('123')
print(inverter)