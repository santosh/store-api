import sqlite3
from flask_restful import Resource, reqparse


class User(object):
    """docstring for User"""
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


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type=str,
        required=True,
        help="Username field can't be left blank!"
    )
    parser.add_argument('password',
        type=str,
        required=True,
        help="Password field can't be left blank!"
    )

    def post(self):
        connection = sqlite3.connect('db.sqlite')
        cursor = connection.cursor()

        data = UserRegister.parser.parse_args()

        if User.find_by_username(data['username']):
            return {'message': 'User with that username already exists.'}, 400

        query = "INSERT INTO users VALUES (NULL, ?, ?)"
        cursor.execute(query, (data['username'], data['password']))

        connection.commit()
        connection.close()

        return {'message': 'User created successfully'}, 201
