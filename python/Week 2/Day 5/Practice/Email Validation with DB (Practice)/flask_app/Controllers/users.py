from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import Email


@app.route("/")
def index():
    return render_template("main.html")


@app.route("/process", methods=["POST"])
def process():
    if not Email.is_valid(request.form):
        return redirect("/")
    Email.save(request.form)
    return redirect("/results")


@app.route("/results")
def results():
    return render_template("dashboard.html", emails=Email.get_all())


@app.route("/clear/<int:id>")
def destroy_email(id):
    data = {"id": id}
    Email.destroy(data)
    return redirect("/results")


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
