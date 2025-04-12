#!/bin/bash

# Ativa o ambiente virtual
source annif-venv/bin/activate

# Instala dependências
pip install --upgrade pip
pip install -r requirements.txt

# Navega para o diretório do ambiente virtual
cd annif-venv

# Ativa o ambiente virtual
source bin/activate

# Executa o servidor na porta 8000 e o torna público (comando no app.py)
#annif run --host 0.0.0.0 --port 8000

# Execute o aplicativo Python (app.py)
python app.py
