# Abra a pasta do seu projeto no terminal
# e digite:
# python -m venv nome_da_pasta

# geralmente é escrito assim: pyhon -m venv venv

# Ativando e desativando meu ambiente virtual

# Windows: .\venv\Scripts\activate
# Linux e Mac: source venv/bin/activate

# Desativar: deactivate


# pip - instalando pacotes e bibliotecas

# Instalar última versão:
# pip install nome_pacote

# Instalar versão precisa
# pip install nome_pacote==0.0.0
# (tem outras formas também não mencionadas)

# Desinstalar pacote
# pip uninstall nome_pacote

# Congelar (ver pacotes)
# pip freeze

# para checar se estamos no venv ou no global: gcm python

print("oi")