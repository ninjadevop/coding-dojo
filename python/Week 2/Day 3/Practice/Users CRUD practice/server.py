from flask import Flask, render_template, redirect, request
from users import User

app = Flask(__name__)

# **** Landing page ****


@app.route("/")
def main():
    return redirect("/users")


@app.route("/users")
def show():
    users = User.get_all()
    return render_template("show.html", users=users)


# **** create page ****
@app.route("/user/new")
def new():
    return render_template("create.html")


# **** action create ****
@app.route("/users/create", methods=["POST"])
def create():
    user_data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
    }
    User.create(user_data)
    return redirect("/users")


# **** one_user page ****
@app.route("/users/<int:id>")
def show_one(id):
    data = {"id": id}
    user = User.get_one(data)
    return render_template("one_user.html", user=user)


# **** action delete ****
@app.route("/users/delete/<int:id>")
def delete(id):
    data = {"id": id}
    data = User.delete(data)
    return redirect("/users")


# **** edit page ****
@app.route("/users/edit/<int:id>")
def update(id):
    data = {"id": id}
    user = User.get_one(data)
    return render_template("edit.html", user=user)


# **** action edit****
@app.route("/users/update/<int:id>", methods=["POST"])
def edit(id):
    data = {
        **request.form,
        "id": id,
    }
    User.edit(data)
    return redirect("/users")


if __name__ == "__main__":
    app.run(debug=True)
