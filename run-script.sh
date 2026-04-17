#!/bin/bash

# Ativa o ambiente virtual
#source annif-venv/bin/activate
# Ativa venv se existir
if [ -d "annif-venv" ]; then
  source annif-venv/bin/activate
fi

# Instala dependências
pip install --upgrade pip
pip install -r requirements.txt

# Garante que Annif está instalado
pip install annif flask uvicorn

# Navega para o diretório do ambiente virtual
cd annif-venv

# Ativa o ambiente virtual
#source bin/activate

# Executa o servidor na porta 8000 e o torna público (comando no app.py)
annif run --host 0.0.0.0 --port 8000
