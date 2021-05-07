from flask import Flask, render_template, send_from_directory
from flask_swagger_ui import get_swaggerui_blueprint
from flask_restful import Api
from dotenv import load_dotenv
from flask_cors import CORS
import os

from app.controllers.c_persona import Persona, PersonaOne

# Add .env file to environment variables used on project
APP_ROOT = os.path.join(os.path.dirname(__file__), '..')
dotenv_path = os.path.join(APP_ROOT, '.env')
load_dotenv(dotenv_path)

app = Flask(__name__)
api = Api(app)
CORS(app)

# Add routes of controllers created in api

SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Test application"
    }
)

app.register_blueprint(swaggerui_blueprint)

api.add_resource(Persona, '/personas')
api.add_resource(PersonaOne, '/personas/<id>')

if __name__ == '__main__':
    app.run(os.getenv("DEBUG"))
