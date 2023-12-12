from flask import Flask

DATABASE = "books_schema"
app = Flask(__name__)
app.secret_key = "shhhhhh"
