from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)


@app.route("/")
def index():
    return render_template("main.html")


@app.route("/users/register", methods=["POST"])
def user_register():
    if not User.validate(request.form):
        return redirect("/")

    pw_hashed = bcrypt.generate_password_hash(request.form["password"])

    data = {**request.form, "password": pw_hashed}

    user_id = User.create(data)
    session["user_id"] = user_id
    return redirect("/dashboard")


@app.route("/users/login", methods=["POST"])
def user_login():
    data = {"email": request.form["email"]}
    user_in_db = User.get_by_email(data)

    if not user_in_db:
        flash("invalid credentials", "log")
        return redirect("/")

    if not bcrypt.check_password_hash(user_in_db.password, request.form["password"]):
        flash("invalid credentials", "log")
        return redirect("/")

    print(f"===> id = {user_in_db.id}")
    session["user_id"] = user_in_db.id
    return redirect("/dashboard")


@app.route("/dashboard")
def dash():
    if "user_id" not in session:
        return redirect("/")
    data = {"id": session["user_id"]}
    loggedin_user = User.get_user_by_id(data)
    session["user_email"] = "a@a.com"
    return render_template("dashboard.html", loggedin_user=loggedin_user)


# ! ------- LOGOUT -------- action
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


# **** one_user page ****
# **** one_user page ****
# **** one_user page ****
# **** one_user page ****
# @app.route("/users/<int:id>")
# def show_one(id):
#     data = {"id": id}
#     user = User.get_one(data)
#     return render_template("one_user.html", user=user)


# # **** action delete ****
# @app.route("/users/delete/<int:id>")
# def delete(id):
#     data = {"id": id}
#     data = User.delete(data)
#     return redirect("/users")


# # **** edit page ****
# @app.route("/users/edit/<int:id>")
# def update(id):
#     data = {"id": id}
#     user = User.get_one(data)
#     return render_template("edit.html", user=user)


# # **** action edit****
# @app.route("/users/update/<int:id>", methods=["POST"])
# def edit(id):
#     data = {
#         **request.form,
#         "id": id,
#     }
#     User.edit(data)
#     return redirect("/users")
