from flask import Flask
from flask_RESTful import Api, Resource

app = Flask(__name__)
api = Api(app)

Book = {
    'book1': {
        'title': 'The Legend of Monkey King', 
        'author': 'Sun Wukong'}
}

class ShowBookList(Resource):
    def get(self):
        return Book

api.add_resource(ShowBookList, '/books')

if __name__ == '__main__':
    app.run(debug=True)
