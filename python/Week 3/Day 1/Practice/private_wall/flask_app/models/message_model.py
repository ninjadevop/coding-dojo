from flask_app.config.mysqlconnection import connectToMySQL
from ..models import user_model
from flask_app import DATABASE

class Message:
    def __init__(self,data):
        self.id=data["id"]
        self.s_user_id=data["s_user_id"]
        self.r_user_id=data["r_user_id"]
        self.message=data["message"]
        self.created_at=data["created_at"]
        self.s_name=user_model.User.get_by_id({'id':self.s_user_id}).first_name

    @classmethod
    def create_message(cls,data):
        query="""INSERT INTO messages 
                            (s_user_id,r_user_id,message)
                            VALUES (%(s_user_id)s,%(r_user_id)s,%(message)s);"""
        return connectToMySQL(DATABASE).query_db(query,data)
    @classmethod
    def get_all_by_id(cls,data):
        query="""SELECT * FROM messages WHERE r_user_id=%(r_user_id)s;"""
        results=connectToMySQL(DATABASE).query_db(query,data)
        all_messages=[]
        for row in results:
            all_messages.append(cls(row))
        return all_messages
    
    
    @classmethod
    def delete_message(cls,data):
        query="""DELETE FROM messages WHERE id=%(id)s"""
        connectToMySQL(DATABASE).query_db(query,data)
        return None