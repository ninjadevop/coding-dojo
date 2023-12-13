from ..config.mysqlconnection import connectToMySQL

class Book:
    def __init__(self,data):
        self.id=data['id']
        self.title=data['title']
        self.num_of_pages=data['num_of_pages']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
    
    @classmethod
    def get_all(cls):
        query="SELECT * FROM books;"
        books=[]
        results=connectToMySQL('books_schema').query_db(query)
        for row in results:
            books.append(cls(row))
        return books
    
    @classmethod
    def save(cls,data):
        query="INSERT INTO books (title,num_of_pages) VALUES (%(title)s,%(num_of_pages)s);"
        return connectToMySQL('books_schema').query_db(query,data)
    
    @classmethod
    def get_one_by_id(cls,data):
        query="SELECT * FROM books WHERE books.id=%(id)s;"
        result=connectToMySQL('books_schema').query_db(query,data)
        return cls(result[0])
    
    @classmethod
    def get_by_favorite_id(cls,data):
        query="SELECT * FROM authors join favorites ON authors.id=favorites.author_id JOIN books ON books.id=favorites.book_id WHERE book_id=%(id)s;"
        favauthors=[]
        results=connectToMySQL('books_schema').query_db(query,data)
        for row in results:
            favauthors.append(row)
        return favauthors
    
    @classmethod
    def fav(cls,data):
        query="INSERT INTO favorites (author_id,book_id) VALUES (%(author_id)s,%(book_id)s);"
        return connectToMySQL('books_schema').query_db(query,data)