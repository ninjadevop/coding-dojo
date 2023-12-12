from flask_app.models.recipe_model import Recipe
from flask_app import app
from flask import Flask, render_template, redirect, request, session, flash
from flask_app.models.user_model import User


@app.route("/recipes")
def all_recipes():
    if "user_id" not in session:
        return redirect("/")
    all_recipes = Recipe.read_all()
    data = {"id": session["user_id"]}
    one_user = User.get_user_by_id(data)
    return render_template("all_recipes.html", all_recipes=all_recipes, user=one_user)


# **** create page ****
@app.route("/recipes/new")
def new():
    if "user_id" not in session:
        return redirect("/")
    return render_template("create_recipe.html")


# **** action create ****
@app.route("/recipes/create", methods=["POST"])
def create():
    if not Recipe.validate(request.form):
        return redirect("/recipes/new")
    recipes_data = {**request.form, "user_id": session["user_id"]}
    Recipe.save(recipes_data)

    return redirect("/recipes")


@app.route("/recipes/<int:id>")
def view_one_recipe(id):
    if "user_id" not in session:
        return redirect("/")
    data = {"id": id}
    recipe_one = Recipe.get_recipe_by_user(data)
    data = {"id": session["user_id"]}
    one_user = User.get_user_by_id(data)
    return render_template("view_one.html", recipe=recipe_one, user=one_user)


# **** edit page ****
@app.route("/recipes/<int:id>/edit")
def update(id):
    if "user_id" not in session:
        return redirect("/")
    data = {"id": id}
    recipe = Recipe.get_recipe_by_user(data)
    return render_template("update_recipe.html", recipe=recipe)


# **** action edit****
@app.route("/recipes/<int:id>/update", methods=["POST"])
def edit_recipe(id):
    if not Recipe.validate(request.form):
        return redirect(f"/recipes/{id}/edit")
    data = {
        **request.form,
        "user_id": session["user_id"],
        "id": id,
    }
    Recipe.edit(data)
    return redirect("/recipes")


# **** action delete ****
@app.route("/recipes/<int:id>/delete", methods=["POST"])
def delete(id):
    data = {
        "id": id,
    }
    Recipe.delete(data)
    return redirect("/recipes")
