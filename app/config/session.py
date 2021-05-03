from sqlalchemy.orm import sessionmaker
from app.config.connection import engine

Session = sessionmaker(bind=engine)
session = Session()