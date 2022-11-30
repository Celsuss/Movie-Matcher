from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
# CORS(app)

# host = os.environ['DB_HOST']
# port = os.environ['DB_PORT']
# user = os.environ['DB_USER']
# password = os.environ['DB_PASSWORD']
# name = os.environ['DB_NAME']
host = 'host'
port = 1111
user = 'user'

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://{}:{}/".format(host, port, user)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

@app.route('/')
def hello():
    return 'Hello World'