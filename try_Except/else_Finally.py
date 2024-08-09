# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions

try:
    print("Try executado")
    # 8/0
except ZeroDivisionError:
    print("Nao divide por 0")
else:
    print("O else executa quando nao tem nenhum erro")
finally: # o finally sempre é executado
    print("Finally executado")