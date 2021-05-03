from flask_restful import reqparse, Resource
from ..models.m_persona import Personas
from ..config.session import session
from flask import json
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
        # print(Persona.query.all())
        return TODOS, 200

    def post(self):

        """Create personas."""
        c1 = Personas(Nombre='Ravi Kumar', Edad=15, Nacimiento='1997-10-10')
        session.add(c1)
        print('hola')
        print(c1)


        session.commit()
        return c1, 201
