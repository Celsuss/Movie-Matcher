from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
CORS(app)

host = os.environ['DB_HOST']
# app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://{}".format(host)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://{}".format(host)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

@app.route('/')
def hello():
    return 'My First API !!'