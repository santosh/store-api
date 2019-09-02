import sqlite3

class UserModel(object):
    """Representation of a user row from users table"""

    def __init__(self, _id, username, password):
        self.id, self.username, self.password = _id, username, password

    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect('db.sqlite')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE username=?"
        result = cursor.execute(query, (username,))
        row = result.fetchone()

        if row:
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user

    @classmethod
    def find_by_id(cls, _id):
        connection = sqlite3.connect('db.sqlite')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE id=?"
        result = cursor.execute(query, (_id,))
        row = result.fetchone()

        if row:
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user

