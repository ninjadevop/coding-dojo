from flask_app.models.book_model import Book
from flask_app import app
from flask import Flask, render_template, redirect, request, session, flash
from flask_app.models.user_model import User


@app.route("/books")
def all_books():
    if "user_id" not in session:
        return redirect("/")
    all_books = Book.read_all()
    data = {"id": session["user_id"]}
    one_user = User.get_user_by_id(data)
    return render_template("all_books.html", all_books=all_books, user=one_user)


# **** create page ****
@app.route("/books/new")
def new():
    if "user_id" not in session:
        return redirect("/")
    return render_template("create_book.html")


# **** action create ****
@app.route("/books/create", methods=["POST"])
def create():
    if not Book.validate(request.form):
        return redirect("/books/new")
    books_data = {
        "title": request.form["title"],
        "author": request.form["author"],
        "my_thoughts": request.form["my_thoughts"],
        "user_id": session["user_id"],
    }
    Book.save(books_data)

    return redirect("/books")


@app.route("/books/<int:id>")
def view_one_book(id):
    if "user_id" not in session:
        return redirect("/")
    data = {"id": id}
    book_one = Book.get_book_by_user(data)
    return render_template("view_one.html", book=book_one)


# **** edit page ****
@app.route("/books/<int:id>/edit")
def update(id):
    if "user_id" not in session:
        return redirect("/")
    data = {"id": id}
    book = Book.get_book_by_user(data)
    return render_template("update_book.html", book=book)


# **** action edit****
@app.route("/books/<int:id>/update", methods=["POST"])
def edit_book(id):
    if not Book.validate(request.form):
        return redirect(f"/books/{id}/edit")
    data = {
        **request.form,
        "user_id": session["user_id"],
        "id": id,
    }
    Book.edit(data)
    return redirect("/books")


# **** action delete ****
@app.route("/books/<int:id>/delete", methods=["POST"])
def delete(id):
    data = {
        "id": id,
    }
    Book.delete(data)
    return redirect("/books")
