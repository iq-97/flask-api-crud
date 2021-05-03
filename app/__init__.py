from flask import Flask, render_template
from flask_restful import Api
import os
from dotenv import load_dotenv

from app.controllers.c_persona import Persona


app = Flask(__name__)
api = Api(app)

# Add .env file to environment variables used on project
APP_ROOT = os.path.join(os.path.dirname(__file__), '..')
dotenv_path = os.path.join(APP_ROOT, '.env')
load_dotenv(dotenv_path)


# Add routes of controllers created in api

api.add_resource(Persona, '/personas')


@app.route('/')
def get_docs():
    # Returns html template of documentation.

    return render_template('swaggerui.html')
