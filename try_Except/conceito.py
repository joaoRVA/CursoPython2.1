# try, except, else e finally
# a = 19
# b = 0
# print(a/b) ZeroDivisionError

try:
    a = 19
    b = 0
    # print('linha1'[10])
    print(a/b)
except ZeroDivisionError as e:
    print(e.__class__.__name__) # retorna o nome do erro
    print(e)
except NameError:
    print("Variável não definida")
except (TypeError, IndexError) as error:
    print("Tipagem ou índice estão errados")
    print('Erro: ', error)
except Exception:
    print("ERRO DESCONHECIDO")