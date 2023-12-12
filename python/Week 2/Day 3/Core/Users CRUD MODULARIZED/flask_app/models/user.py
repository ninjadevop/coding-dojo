from flask_app.config.mysqlconnection import connectToMySQL

db = "users_schema"


class User:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def get_all(cls):
        query = "select * from users ;"
        results = connectToMySQL(db).query_db(query)
        users = []
        for i in results:
            users.append(cls(i))
        return users

    @classmethod
    def create(cls, data):
        query = """
                INSERT INTO users (first_name, last_name, email)
                values (%(first_name)s,%(last_name)s,%(email)s);
            """
        resu = connectToMySQL(db).query_db(query, data)
        return resu

    @classmethod
    def get_one(cls, data):
        query = """
                select * from users
                where id = %(id)s;
            """
        results = connectToMySQL(db).query_db(query, data)
        user = cls(results[0])
        return user

    @classmethod
    def edit(cls, data):
        query = """
                update users 
                set first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s
                where id=%(id)s;
            """
        results = connectToMySQL(db).query_db(query, data)
        return results

    @classmethod
    def delete(cls, data):
        query = """
                delete from users 
                where id=%(id)s;
        """
        results = connectToMySQL(db).query_db(query, data)
        return results
