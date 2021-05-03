from sqlalchemy import create_engine
from os import getenv

engine = create_engine(getenv("SQLALCHEMY_DATABASE_URI"))
