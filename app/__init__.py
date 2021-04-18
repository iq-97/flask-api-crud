from flask import Flask
from app.controllers.c_persona import r_persona

app = Flask(__name__)

# Creation of Routes
app.register_blueprint(r_persona, url_prefix='/personas')



