from flask import Flask
from app.controllers.Controller1 import example_blueprint

app = Flask(__name__)
app.register_blueprint(example_blueprint)

app.run()

