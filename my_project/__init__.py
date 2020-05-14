import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)

app.config["SECRET_KEY"] = "mysecretkey"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///"+os.path.join(BASE_DIR, "data.sqlite")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
Migrate(app, db)

from my_project.puppies.views import puppies_blueprint
from my_project.owners.views import owners_blueprint

app.register_blueprint(puppies_blueprint, url_prefix="/puppies")
app.register_blueprint(owners_blueprint, url_prefix="/owners")