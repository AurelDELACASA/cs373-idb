rm -rf app/venv
virtualenv -p /usr/bin/python3.5 app/venv/
source app/venv/bin/activate
pip3 install flask flask_sqlalchemy psycopg2
python3.5 app/app.py
