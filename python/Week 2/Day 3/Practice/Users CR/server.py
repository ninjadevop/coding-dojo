from flask import Flask, render_template, redirect, request
from user import User

app = Flask(__name__)


# * DISPLAY ROUTE - # RENDER
@app.route("/users")
def display_form():
    return render_template("create.html")


#! ACTION ROUTE - # CREATE
@app.route("/users/new", methods=["post"])
def creat_user():
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
    }
    User.creat_user(data)

    return redirect("/")


#! ACTION ROUTE - # read
@app.route("/")
def read():
    all_users = User.get_all()
    return render_template("read.html", users=all_users)


if __name__ == "__main__":
    app.run(debug=True)
