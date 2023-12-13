from ..config.mysqlconnection import connectToMySQL

class Author:
    def __init__(self,data):
        self.id=data['id']
        self.first_name=data['first_name']
        self.last_name=data['last_name']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
    
    @classmethod
    def get_all(cls):
        query="SELECT * FROM authors;"
        authors=[]
        results=connectToMySQL('books_db').query_db(query)
        for row in results:
            authors.append(cls(row))
        return authors
    
    @classmethod
    def save(cls,data):
        query="INSERT INTO authors(first_name,last_name) VALUES (%(first_name)s,%(last_name)s);"
        return connectToMySQL('books_db').query_db(query,data)
    
    @classmethod
    def get_one_by_id(cls,data):
        query="SELECT * FROM authors WHERE id=%(id)s;"
        result=connectToMySQL('books_db').query_db(query,data)
        return cls(result[0])
    
    @classmethod
    def get_by_favorite_id(cls,data):
        query="SELECT * FROM authors join favorites ON authors.id=favorites.author_id JOIN books ON books.id=favorites.book_id WHERE author_id=%(id)s;"
        favbooks=[]
        results=connectToMySQL('books_db').query_db(query,data)
        for row in results:
            favbooks.append(row)
        return favbooks
    
    @classmethod
    def fava(cls,data):
        query="INSERT INTO favorites (author_id,book_id) VALUES (%(author_id)s,%(book_id)s);"
        return connectToMySQL('books_db').query_db(query,data)
    