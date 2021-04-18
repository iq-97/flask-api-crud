from flask import Blueprint

r_persona = Blueprint('example_blueprint', __name__)


@r_persona.route('/', methods=['GET'])
def index():
    return "This is an example app"
