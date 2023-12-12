# __init__.py
from flask import Flask

DATABASE = "emails_schema"
app = Flask(__name__)
app.secret_key = "shhhhhh"
