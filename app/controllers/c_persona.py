from flask_restful import reqparse, Resource
import os

TODOS = {
    'todo1': {'task': 'build an API'},
    'todo2': {'task': '?????'},
    'todo3': {'task': 'profit!'},
}

parser = reqparse.RequestParser()
parser.add_argument('task')

# Class of personas
# CRUD de personas

class Persona(Resource):

    def get(self):

        """Returned list of personas."""
        print(f'API_KEY = {os.getenv("API_KEY")}')
        return TODOS, 200

    def post(self):

        """Create personas."""
        args = parser.parse_args()
        todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
        todo_id = 'todo%i' % todo_id
        TODOS[todo_id] = {'task': args['task']}
        return TODOS[todo_id], 201
