from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://appdesafiado@python-desafiado:&Bd825212@python-desafiado.mysql.database.azure.com/python-desafiado'

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://Keran@apipython:&Bd825212@apipython.mysql.database.azure.com/apipython'

db = SQLAlchemy(app)
