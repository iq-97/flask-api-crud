from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from app.models.m_persona import Personas


class PersonaSchema(SQLAlchemySchema):
    class Meta:
        model = Personas
        load_instance = True  # Optional: deserialize to model instances

    id = auto_field()
    Nombre = auto_field()
    Edad = auto_field()
    Nacimiento = auto_field()