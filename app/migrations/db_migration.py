from sqlalchemy import MetaData, Table, Column, Integer, String, DateTime
meta = MetaData()

Personas = Table(
   'Personas', meta,
   Column('id', Integer, primary_key=True),
   Column('Nombre', String(25)),
   Column('Edad', Integer),
   Column('Nacimiento', DateTime),
)
