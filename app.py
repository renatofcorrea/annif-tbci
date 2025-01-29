from flask import Flask
import connexion
import subprocess
import os

app = Flask(__name__)
connexion_app = connexion.FlaskApp(__name__, specification_dir='./')
# Adicionar suas rotas e especificações de API
#connexion_app.add_api('swagger.yaml')

@app.route("//workspaces/codespaces-flask/annif-venv/")
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    # Configurar a porta pública padrão
    port = int(os.environ.get('PORT', 8000))
    # Navegar até o diretório do ambiente virtual
    os.chdir('/workspaces/codespaces-flask/annif-venv')
    # Ativar o ambiente virtual
    #subprocess.run(['source', 'annif-venv/bin/activate'], shell=True)
    activate_script = os.path.join(os.getcwd(), 'bin/activate')
    # Executar o Annif
    command = f'. {activate_script} && annif run --host 127.0.0.1 --port {port}'
    subprocess.run(command, shell=True, check=True)
    #subprocess.run(['annif', 'run', '--host', '127.0.0.1', '--port', '5000'])
    # Inicializar o servidor Flask (mantém o processo ativo)
    app.run(host='127.0.0.1', port=5000)