from flask_app import app
from flask import redirect,request,render_template,url_for
from flask_app.models.author import Author
from flask_app.models.book import Book




@app.route('/')
def index():
    return redirect('/authors')

@app.route('/authors')
def authors():
    all_authors=Author.get_all()
    return render_template('authors.html',all_authors=all_authors)


@app.route('/create/author',methods=["post"])
def create_author():
    data={"first_name":request.form['first_name'],"last_name":request.form['last_name']}
    Author.save(data)
    return redirect('/authors')

@app.route('/authors/<int:id>')
def author_details(id):
    data= {
        "id":id
    }
    return render_template('one_author.html',author=Author.get_one_by_id(data),favbooks=Author.get_by_favorite_id(data),all_books=Book.get_all())

@app.route('/favoriteauthor/add',methods=["post"])
def favorite_author():
    data={"book_id":request.form['book_id'],"author_id":request.form['author_id']}
    Author.fava(data)
    return redirect(url_for('author_details',id=data['author_id']))