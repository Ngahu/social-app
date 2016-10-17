from flask import Flask, g
import models


DEBUG = True
PORT = 8000
HOST = '0.0.0.0'


app = Flask(__name__)


@app.before_request
def before_request():
    """Connect to the database before each request"""
    g.db = models.DATABASE
    g.db.Connect()
