from flask import Flask
from peewee import *
from flask.ext.cors import CORS
from flask.ext.compress import Compress

usuario, senha = 'root', '87654321'
host, banco = 'localhost', 'gdsw_matricula'

app = Flask(__name__)
CORS(app)
Compress(app)

db = MySQLDatabase(
            banco,
            user=usuario,
            passwd=senha,
            #host=host,
    )

db.get_conn().ping(True)

# This hook ensures that a connection is opened to handle any queries
# generated by the request.
@app.before_request
def _db_connect(a):
    db.connect()
    print("A conexão com o banco foi aberta.")

# This hook ensures that the connection is closed when we've finished
# processing the request.
@app.teardown_request
def _db_close(a):
    if not db.is_closed():
        db.close()
        print("A conexão com o banco foi fechada.")
