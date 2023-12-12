from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello World!"


@app.route("/<name>")
def dojo(name):
    return "Dojo!"


@app.route("/say/<name>")
def say(name):
    return "Hi " + name + "!"


@app.route("/repeat/<int:num>/<names>")
def repeat(num, names):
    return num * names


if __name__ == "__main__":
    app.run(debug=True)
