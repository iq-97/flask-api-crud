from flask_restful import reqparse, Resource
from app.models.m_persona import Personas
from app.schemas.s_persona import PersonaSchema
from app.config.session import session
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

class PersonaOne(Resource):

    def get(self, id):
        _persona = session.query(Personas).get(id)
        _schema = PersonaSchema()
        data = PersonaSchema().dump(_persona)
        print(data)

        return data, 200

    def delete(self, id):
        _persona = session.query(Personas).filter(Personas.id == id).first()
        session.delete(_persona)
        session.commit()

        return id, 204

    def put(self, id):
        _persona = session.query(Personas).filter(Personas.id == id).first()
        _persona.Nombre = 'Hola Actualizado'
        _persona.Edad = 19
        _persona.Nacimiento = '1998-11-11'
        session.commit()

        return id, 201