# caminho_arquivo = 'D:\\Documentos\\'
caminho_arquivo = 'CriacaoArquivo\\arquivo.txt'

# arquivo = open(caminho_arquivo, 'w')
# #
# arquivo.close() FECHAR O ARQUIVO SEMPRE, SENAO DA MERDA

# abrir o arquivo com with, ja abre e fecha automaticamente

#Sintaxe: with open(caminho, modo('w', 'r', etc)) as variavel
# "w+" ativa o modo de leitura

with open(caminho_arquivo, 'w+') as arquivo:
    arquivo.write("linha 1\n")
    arquivo.seek(0,0) # o seek serve para mover o cursor, no caso até o inicio
    print(arquivo.read(), end='') # end='' para não ler a quebra de linha
    arquivo.write("linha 2\n")
    arquivo.writelines(
        ("linha 3\n", "linha 4\n")
    )
    arquivo.seek(0,0)
    print("-" * 20)
    print(arquivo.readline().strip()) # readline() lê uma linha por vez, strip() remove espaços em branco
    print(arquivo.readline().strip())
    print(arquivo.readline().strip())
    print(arquivo.readline().strip())
    print("-" * 20) 
    arquivo.seek(0,0)
    for proxima_linha in arquivo.readlines(): # readlines() lê uma lista de linhas []
        print(proxima_linha.strip())



# o modo "a" permite adicionar escrita no ao final do arquivo, sem apagar o que tinha antes
with open(caminho_arquivo, 'a+', encoding="utf8") as arquivo:
    print("-" * 20) 
    arquivo.write("continuando...\n")
    arquivo.write("Atenção\n") # o encoding do windows não lê caracteres especiais, UTF-8 é o melhor
    arquivo.seek(0,0)
    print(arquivo.read().strip())


# módulo os
# os.remove ou os.unlink - remove um arquivo
# os.rename() - renomear arquivo
import os
# os.remove(caminho_arquivo)
# os.rename(caminho_arquivo, "CriacaoArquivo\\novo_arquivo.txt")