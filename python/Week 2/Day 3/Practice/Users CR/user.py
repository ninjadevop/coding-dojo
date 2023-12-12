from mysqlconnection import connectToMySQL
from pprint import pprint

DATABASE = "users_schema"


class User:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    # create
    @classmethod
    def creat_user(cls, data):
        query = """
            INSERT INTO USERS (first_name, last_name, email)
            values (%(first_name)s,%(last_name)s,%(email)s );
            """
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result

    # READ
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM   USERS;"

        all_users = connectToMySQL(DATABASE).query_db(query)

        users = []
        for i in all_users:
            one_user = cls(i)
            users.append(one_user)
        return users
