from flask import Flask
from peewee import *

usuario, senha = 'root', '87654321'
host, banco = 'localhost', 'gdsw_matricula'
db = MySQLDatabase(
            banco,
            user=usuario,
            passwd=senha,
            #host=host,
    )

def before_request_handler():
    db.connect()

def after_request_handler():
    db.close()
