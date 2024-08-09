# Exercício - Lista de tarefas com desfazer e refazer
 

# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

# lista = []

# lista.append(1)
# lista.append(2)
# print(lista)
# ultimo = lista.pop()
# print(lista)
# print(ultimo)


# listar, desfazer e refazer
import os
import json

ARQUIVO = "listar_desfazer_refazer\\lista_tarefas.json"

def ler(caminho, list):
    dados = []
    try:
        with open(caminho, "r", encoding="utf8") as tarefas:
            dados = json.load(tarefas)
    except FileNotFoundError:
        salvar(caminho, list)
    return dados


def salvar(caminho, list):
    dados = list
    with open(caminho, "w", encoding="utf8") as tarefas:
        dados = json.dump(list, tarefas, indent=2, ensure_ascii=False)
    return dados


lista = ler(ARQUIVO, []) # vai tentar ler o arquivo ao criar a variavel
lista_refazer = []
while True:




    print("\nlista de Tarefas")
    print()
    tarefa = str(input("Digite a tarefa desejada:\n  (1)adicionar | (2)desfazer | (3)refazer ").lower())
    os.system('cls')
    if tarefa == 'adicionar' or tarefa == '1':
        os.system('cls')
        valor = input("Digite a tarefa: ")
        lista.append(valor)
        print('======Lista======')
        print(*lista, sep='\n')
        print('=================')

        salvar(ARQUIVO, lista)

    elif tarefa == 'desfazer' or tarefa == '2':
        if lista == []:
            os.system('cls')
            print("lista ainda vazia.")
            
        else:
            valor_excluido = lista.pop()
            lista_refazer.append(valor_excluido)
            print('======Lista======')
            print(*lista, sep='\n')
            print('=================')
            salvar(ARQUIVO, lista)


    elif tarefa == 'refazer' or tarefa == '3':
        if lista_refazer == []:
            os.system('cls')
            print('não tem nada para refazer')
        else:
            refazer = lista_refazer.pop()
            lista.append(refazer)
            print('======Lista======')
            print(*lista, sep='\n')
            print('=================')
            salvar(ARQUIVO, lista)

    else:
        print("Você não digitou corretamente, recomeçando programa...")
        