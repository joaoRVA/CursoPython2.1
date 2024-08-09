# JSON - JavaScript Object Notation
# É uma estrutura de dados que serve para salvar ou transportar os dados.

# JSON suporta poucos tipos de dados, porque ele é muito simples
# Tipos de dados suportáveis:
# 123 - int
# 12.3 - float(mas ele entende como int)
# [] - listas
# {} - dicionários
# "Joao" - string
# () - tupla(ele converte em lista dps)
import json

pessoa = {
    'nome': 'PênisValdo',
    'sobrenome': 'Rodrigues',
    'enderecos': [
        {'rua': 'R1', 'numero': 32},
        {'rua': 'R2', 'numero': 55},
    ],
    'altura': 1.75,
    'numeros_preferidos': (2, 4, 6, 8, 10),
    'dev': True,
    'nada': None,
}
caminho = "JSON_\\arquivo.json"

with open(caminho, "w", encoding="utf8") as file:
    json.dump(pessoa, file, indent=2, ensure_ascii=False) # sintaxe: json.dump(tipo_de_dado, receber_dado, indent=2)


with open(caminho, 'r', encoding="utf8") as arquivo:
    pessoa = json.load(arquivo) # json.load(nome do arquivo) para ler os dados do arquivo json
    print(pessoa['nome'])