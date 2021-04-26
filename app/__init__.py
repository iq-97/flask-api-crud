from flask import Flask, render_template
from flask_restful import reqparse, abort, Api, Resource

from app.controllers.c_persona import Persona

app = Flask(__name__)
api = Api(app)

##
## Actually setup the Api resource routing here
##


@app.route('/')
def get_docs():
    return render_template('swaggerui.html')


api.add_resource(Persona, '/personas')
