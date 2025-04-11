source annif-venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
cd annif-venv
source bin/activate
annif run --host 0.0.0.0 --port 8000
