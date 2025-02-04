from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS   # laat ons een request sturen vanuit een andere url

app = Flask(__name__) # om de flask aplicatie te initialiseren
CORS(app) # om een bepaalde error uit te schakelen

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///userInfo.db"   # maken de locatie van de database aan
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False    # we gaan de modificaties van de database niet tracken

db = SQLAlchemy(app)    # om toegang te krijgen tot de database (mydatabase.db)