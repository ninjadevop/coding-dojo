# users.py
from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.user import User


@app.route(
    "/"
)  # The "@" decorator associates this route with the function immediately following
def get_all_users():
    all_users = User.get_all()
    print(all_users)
    return render_template("index.html", users=all_users)


# * DISPLAY ROUTE - RENDER
@app.route(
    "/form"
)  # The "@" decorator associates this route with the function immediately following
def display_form():
    return render_template("form.html")


#! ACTION ROUTE - CREATE
@app.route(
    "/create", methods=["POST"]
)  # The "@" decorator associates this route with the function immediately following
def create_user():
    # print(request.form)
    user_dict = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
    }
    User.save(user_dict)
    return redirect("/")


# * DISPLAY ROUTE - RENDER
@app.route("/show/<int:id>")
def show_one(id):
    data = {"id": id}
    user = User.get_one(data)
    return render_template("show.html", user=user)


# * DISPLAY ROUTE - RENDER
@app.route("/edit/<int:id>")
def update_user(id):
    user_id_dict = {"id": id}
    user = User.get_one(user_id_dict)
    return render_template("edit.html", user=user)


#! ACTION ROUTE
@app.route("/update/<int:id>", methods=["POST"])
def process_update(id):
    data = {
        **request.form,
        "id": id,
    }
    User.update(data)
    return redirect("/")