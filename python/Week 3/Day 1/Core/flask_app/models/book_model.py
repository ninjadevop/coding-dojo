from flask_app import DATABASE
from flask_app.config.mysqlconnection import connectToMySQL
from flask import Flask, render_template, redirect, request, session, flash
from flask_app.models import user_model


class Book:
    def __init__(self, data):
        self.id = data["id"]
        self.title = data["title"]
        self.author = data["author"]
        self.my_thoughts = data["my_thoughts"]
        self.user_id = data["user_id"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.creator = None

    #! READ ALL

    @classmethod
    def read_all(cls):
        query = """
            SELECT * FROM books
            JOIN users
            ON users.id = books.user_id;
            """
        results = connectToMySQL(DATABASE).query_db(query)

        books = []
        for row in results:
            one_book = cls(row)
            fixed_user = {
                "id": row["users.id"],
                "name": row["name"],
                "email": row["email"],
                "password": row["password"],
                "created_at": row["users.created_at"],
                "updated_at": row["users.updated_at"],
            }

            one_book.creator = user_model.User(fixed_user)
            books.append(one_book)

        return books

    @classmethod
    def get_book_by_user(cls, data):
        query = """
            SELECT * FROM books
            JOIN users
            ON users.id = books.user_id
            where books.id = %(id)s;
            """
        results = connectToMySQL(DATABASE).query_db(query, data)
        one_book = cls(results[0])
        fixed_user = {
            "id": results[0]["users.id"],
            "name": results[0]["name"],
            "email": results[0]["email"],
            "password": results[0]["password"],
            "created_at": results[0]["users.created_at"],
            "updated_at": results[0]["users.updated_at"],
        }
        one_book.creator = user_model.User(fixed_user)
        return one_book

    @classmethod
    def save(cls, data):
        query = """INSERT INTO books (title,author,my_thoughts, user_id)
                values (%(title)s,%(author)s,%(my_thoughts)s,%(user_id)s ); 
            """
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def edit(cls, data):
        query = """
                update books
                set title = %(title)s, author = %(author)s, my_thoughts=%(my_thoughts)s, user_id=%(user_id)s
                where id=%(id)s;
            """
        results = connectToMySQL(DATABASE).query_db(query, data)
        return results

    @classmethod
    def delete(cls, data):
        query = """
                delete from books 
                where id=%(id)s;
        """
        results = connectToMySQL(DATABASE).query_db(query, data)
        return results

    @staticmethod
    def validate(data):
        is_valid = True

        if len(data["title"]) < 2:
            is_valid = False
            flash("title must not be blank")
        if len(data["author"]) < 2:
            is_valid = False
            flash("Author must not be blank")

        if len(data["my_thoughts"]) < 2:
            is_valid = False
            flash("my_thoughts must not be blank")

        return is_valid
