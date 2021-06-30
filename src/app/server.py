from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://janaina@pythondbapi:#BrunoPhelipe@pythondbapi.mysql.database.azure.com/pythondbapi'


db = SQLAlchemy(app)
