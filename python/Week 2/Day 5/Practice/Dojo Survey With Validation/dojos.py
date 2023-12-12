from mysqlconnection import connectToMySQL

DATABASE = "dojo_survey_schema"


class Dojo:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.location = data["location"]
        self.language = data["language"]
        self.comment = data["comment"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def create(cls, data):
        query = """
                INSERT INTO dojos (name, location, language,comment)
                values (%(name)s,%(location)s,%(language)s),%(comment)s);
            """
        resu = connectToMySQL(DATABASE).query_db(query, data)
        return resu

    @staticmethod
    def validate(data):
        is_valid = True

        if len(data["name"]) < 1:
            is_valid = False
            flash("name must not be blank")
        if len(data["location"]) < 1:
            is_valid = False
            flash("You must choose a location")

        if len(data["language,"]) < 1:
            is_valid = False
            flash("You must choose a language")

        if len(data["comment"]) < 1:
            is_valid = False
            flash("comment must not be blank")
        return is_valid

    if __name__ == "__main__":
        app.run(debug=True)
