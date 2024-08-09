# Modularização - Entendendo os seus próprios módulos Python
# O primeiro módulo executado chama-se __main__
# Você pode importar outro módulo inteiro ou parte do módulo
# O python conhece a pasta onde o __main__ está e as pastas
# abaixo dele.
# Ele não reconhece pastas e módulos acima do __main__ por
# padrão
# O python conhece todos os módulos e pacotes presentes
# nos caminhos de sys.path


try:
    import sys
    sys.path.append('C:/Users/joaov/Desktop') # adicionei um novo caminho de busca para o python
    # import modulo_desktop # importei o aquivo.py que criei na area de trabalho
except ModuleNotFoundError:
    print("modulo não encontrado")

    
import modularização_2
from modularização_2 import somar, a, b
print("Este é o módulo:", __name__)

# print(*sys.path, sep='\n') # esses são os caminhos aonde o python procura módulos

print(modularização_2.a + modularização_2.b)
print(a + b)
print(somar(5, 6))