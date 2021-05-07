from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Personas(Base):
    __tablename__ = 'Personas'

    id = Column(Integer, primary_key=True)
    Nombre = Column(String(25))
    Edad = Column(Integer)
    Nacimiento = Column(DateTime)

    def __repr__(self):
        return "<Personas(Nombre={self.Nombre!r}, Edad={self.Edad!r}, Nacimiento={self.Nacimiento!r})>".format(self=self)

    def __init__(self, Nombre, Edad, Nacimiento):
        self.Nombre = Nombre
        self.Edad = Edad
        self.Nacimiento = Nacimiento

