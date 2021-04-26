from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

from app.controllers.c_persona import Persona

app = Flask(__name__)
api = Api(app)

##
## Actually setup the Api resource routing here
##
api.add_resource(Persona, '/personas')
