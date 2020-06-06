from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_restful import fields, marshal_with

app = Flask(__name__)
api = Api(app)

todos = {}

class Todo1(Resource):
    def get(self):
        # Default to 200 OK
        return {'task': 'Hello world_1'}

class Todo2(Resource):
    def get(self):
        # Set the response code to 201
        return {'task': 'Hello world_2'}, 201

class Todo3(Resource):
    def get(self):
        # Set the response code to 201 and return custom headers
        return {'task': 'Hello world_3'}, 201, {'Etag': 'some-opaque-string'}

class Todo5(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('rate', type=int, help='Rate to charge for this resource')
        args = parser.parse_args()

        return parser.parse_args()

resource_fields = {
    'task':   fields.String,
    'uri':    fields.Url('todo_ep')
}

class TodoDao(object):
    def __init__(self, todo_id, task):
        self.todo_id = todo_id
        self.task = task

        # This field will not be sent in the response
        self.status = 'active'

class Todo(Resource):
    @marshal_with(resource_fields)
    def get(self, **kwargs):
        return TodoDao(todo_id='my_todo', task='Remember the milk')

api.add_resource(Todo1, '/todo1')
api.add_resource(Todo2, '/todo2')
api.add_resource(Todo3, '/todo3', '/todo4')

api.add_resource(Todo5, '/todo5')
api.add_resource(Todo,
    '/todo/<int:todo_id>')


if __name__ == '__main__':
    app.run(debug=True)