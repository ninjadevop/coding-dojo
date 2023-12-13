from flask_app import app
from flask import redirect,request,render_template
from flask_app.models.author import Author
from flask_app.models.book import Book


@app.route('/books')
def books():
    all_books=Book.get_all()
    return render_template('/books.html',all_books=all_books)

@app.route('/create/book',methods=["post"])
def create_book():
    data={"title":request.form['title'],"num_of_pages":request.form['num_of_pages']}
    Book.save(data)
    return redirect('/books')


@app.route('/books/<int:id>')
def book_details(id):
    data= {
        "id":id
    }
    return render_template('one_book.html',book=Book.get_one_by_id(data),favauthors=Book.get_by_favorite_id(data),all_authors=Author.get_all())

@app.route('/favoritebook/add',methods=["post"])
def favorite_book():
    data={"book_id":request.form['book_id'],"author_id":request.form['author_id']}
    Book.fav(data)
    return redirect(url_for('book_details',id=data['book_id']))