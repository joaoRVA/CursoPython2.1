# da pra lançar nosso proprios erros

# RAISE

def nao_aceito_zero(b):
    if b == 0:
        raise ZeroDivisionError("Você está tentando dividir por zero")
    return True

def deve_ser_int_ou_float(n):
    tipo_n = type(n)
    if not isinstance(n, (float, int)):
        raise TypeError(
            f'"{n}" deve ser int ou float. '
            f'"{tipo_n.__name__}" enviado.'
        )
    return True

def divide(a, b):
    deve_ser_int_ou_float(a)
    deve_ser_int_ou_float(b)
    nao_aceito_zero(b)
    return a/b

num1 = divide(4, 0)

print(num1)