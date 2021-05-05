from flask_restful import reqparse, Resource
from app.models.m_persona import Personas
from app.schemas.s_persona import PersonaSchema
from app.config.session import session
import json
parser = reqparse.RequestParser()
parser.add_argument('task')

# Class of personas
# CRUD de personas


class Persona(Resource):

    def get(self):
        """Returned list of personas."""
        _personas = session.query(Personas).all()
        _schema = PersonaSchema()
        data = PersonaSchema(many=True).dump(_personas)
        return data, 200

    def post(self):
        """Create personas."""
        _persona = Personas(Nombre='Ravi Kumar', Edad=15, Nacimiento='1997-10-10')
        _schema = PersonaSchema()

        session.add(_persona)
        session.commit()
        return _schema.dump(_persona), 201
