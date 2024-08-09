# Para criar uma api que todos possam usar, é necessário fazer deploy após ser criada.

# deploy = colocar o programa para que todos possam usar

# então, vamos usar um site que faz o deploy automaticamente: www.replit.com



"""
import pandas as pd
from flask import Flask, jsonify

# Inicializa o Flask
app = Flask(__name__)

# Constrói as funcionalidades
@app.route('/')
def homepage():
  return 'A API está no ar'

@app.route('/pegarvendas')
def pegarvendas():
  tabela = pd.read_csv('advertising.csv')
  total_vendas = tabela['Vendas'].sum()
  dict_vendas = {"total vendas": total_vendas}
  return jsonify(dict_vendas)

  
# rodar o site/API
# host='0.0.0.0' para rodar no replit
app.run(host='0.0.0.0')
"""

# https://0bf69a86-4b92-4659-8a6c-2de790fd25d5-00-1x9d9b5dbfgtk.janeway.replit.dev/pegarvendas

import requests

pegar_endpoint = requests.get("https://0bf69a86-4b92-4659-8a6c-2de790fd25d5-00-1x9d9b5dbfgtk.janeway.replit.dev/pegarvendas")

transforma_json = pegar_endpoint.json()

print(transforma_json['total vendas'])