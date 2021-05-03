from flask import Flask, render_template
from flask_restful import Api
from dotenv import load_dotenv
from sqlalchemy import create_engine
import os

from app.controllers.c_persona import Persona

# Add .env file to environment variables used on project
APP_ROOT = os.path.join(os.path.dirname(__file__), '..')
dotenv_path = os.path.join(APP_ROOT, '.env')
load_dotenv(dotenv_path)

engine = create_engine(os.getenv("SQLALCHEMY_DATABASE_URI"))

app = Flask(__name__)
api = Api(app)

# Add routes of controllers created in api

api.add_resource(Persona, '/personas')

@app.route('/')
def get_docs():
    # Returns html template of documentation.

    return render_template('swaggerui.html')