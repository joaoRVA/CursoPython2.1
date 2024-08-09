import recarregar2
# os modulos do python são singleton, ou seja, só carregam na memória 1 vez e ja era
# se quiser recarregar, utilize o modulo importlib

import importlib
for i in range(10):
    importlib.reload(recarregar2)



print("ACABOU")