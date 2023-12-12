from flask import Flask, render_template, redirect, request, session, flash
from dojos import Dojo
from mysqlconnection import connectToMySQL


app = Flask(__name__)
app.secret_key = "your_secret_key"  # Change this to a secure secret key


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/process", methods=["POST"])
def process():
    if not Dojo.validate(request.form):
        return redirect("/")
    session["name"] = request.form["name"]
    session["location"] = request.form["location"]
    session["favorite_language"] = request.form["language"]
    session["comments"] = request.form["comments"]
    return redirect("/result")


@app.route("/result")
def result():
    return render_template("result.html")


@app.route("/clear")
def clear():
    session.clear()
    return redirect("/")
