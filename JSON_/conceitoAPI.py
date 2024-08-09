# API - Application Programming Interface

# É um meio de comunicação entre o servidor e o programador
# Onde vamos conseguir pegar ou enviar dados no formato JSON para fazer um determinado sistema.

# Vou pedir informações pra API e ela vai me entregar

# Exemplo de como pegar dados de um API:

# 1º passo: instalar o módulo requests - pip install requests

import requests

# 2º passo: pegar informações da api de cotação de dólar - requests.get()

requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
print(requisicao)
# por padrão, PRIMEIRO as APIs retornam se deu certo ou se deu errado, no caso dessa: 200 deu certo / 404 deu errado

# Então temos que armazenar em uma variável a api em formato de json
dic_requisicao = requisicao.json()

# 3º passo: vamos fazer um dump para transformar essa api em um arquivo
import json
caminho = "JSON_\\moeda.json"
with open(caminho, "w", encoding="utf8") as moedas:
    json.dump(dic_requisicao, moedas, indent=2, ensure_ascii=False)


# 4º passo: pegar a cotação do dolar

with open(caminho, 'r', encoding="utf8") as dolar:
    cotacao = json.load(dolar)
    print(cotacao['USDBRL']['bid'])