from sqlalchemy.orm import scoped_session, sessionmaker
from app.config.connection import engine

# Session = sessionmaker(bind=engine)
session = scoped_session(sessionmaker(bind=engine))