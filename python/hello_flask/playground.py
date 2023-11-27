from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "hello world!"


@app.route("/play")
def play():
    return render_template("index.html")


@app.route("/play/<int:num>/<string:color>")
def root(num , color):
    return render_template("index.html", num=num, color = color)


if __name__ == "__main__":
    app.run(debug=True)
