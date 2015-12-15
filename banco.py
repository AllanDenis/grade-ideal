from flask import Flask
from peewee import *

usuario, senha = 'root', '87654321'
host, banco = 'localhost', 'gdsw_matricula'

app = Flask(__name__)

db = MySQLDatabase(
            banco,
            user=usuario,
            passwd=senha,
            #host=host,
    )

# This hook ensures that a connection is opened to handle any queries
# generated by the request.
@app.before_request
def _db_connect():
    db.connect()

# This hook ensures that the connection is closed when we've finished
# processing the request.
@app.teardown_request
def _db_close():
    if not db.is_closed():
        db.close()
