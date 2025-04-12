from flask import Flask
#import connexion
import subprocess
import os

app = Flask(__name__)
#connexion_app = connexion.FlaskApp(__name__, specification_dir='./')

@app.route("/")

def home():
    # Carrega a interface do Annif
    # Configurar a porta pública padrão
    port = 8000 #int(os.environ.get('PORT', 8000))
    host = '0.0.0.0'
    # Nome do diretório alvo
    target_dir = "annif-venv"
    # Verifica se o diretório corrente já termina com 'annif-venv'
    if os.getcwd().endswith(target_dir):
        # Navegar até o diretório do ambiente virtual
        os.chdir(os.getcwd())
        print("Diretório atual:"+ os.getcwd())
    else:
        # Navega para o diretório 'annif-venv' caso não esteja
        new_path = os.path.join(os.getcwd(), target_dir)
        #s.chdir(os.getcwd()+'/annif-venv')
        if os.path.exists(new_path):
            os.chdir(new_path)
            print(f"Diretório alterado para: {os.getcwd()}")
        else:
            print(f"O diretório '{target_dir}' não existe no caminho atual:"+os.getcwd())
    activate_script = os.path.join(os.getcwd(), 'bin/activate')
    # Executar o Annif
    command = f'. {activate_script} && annif run --host {host} --port {port}'
    subprocess.run(command, shell=True, check=True)
    return "Executando o Annif!"

if __name__ == '__main__':
    # Configurar a porta pública padrão
    port = int(os.environ.get('PORT', 8000))
    host = '0.0.0.0'
    """
    # Navegar até o diretório do ambiente virtual
    os.chdir(os.getcwd()+'/annif-venv')
    # Ativar o ambiente virtual
    #subprocess.run(['source', 'annif-venv/bin/activate'], shell=True)
    activate_script = os.path.join(os.getcwd(), 'bin/activate')
    # Executar o Annif
    command = f'. {activate_script} && annif run --host {host} --port {port}'
    subprocess.run(command, shell=True, check=True)
    #subprocess.run(['annif', 'run', '--host', '127.0.0.1', '--port', '5000'])
    # Inicializar o servidor Flask (mantém o processo ativo)
    """
    app.run(host=host, port=port)