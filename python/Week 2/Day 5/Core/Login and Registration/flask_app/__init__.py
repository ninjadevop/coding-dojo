# __init__.py
from flask import Flask

DATABASE = "recipes_schema"
app = Flask(__name__)
app.secret_key = "shhhhhh"
