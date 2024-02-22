from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from flask_migrate import Migrate
from models import db
from properties import Property, SpecificProperty


app = Flask(__name__)

api = Api(app)
app.json.compact = False

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///jeddy_database.db"

app.secret_key = 'f56213769831da626afe38f227127d0645df08dd07d31e170a7c6ae44961d4d8'

migrate = Migrate(app  , db)

CORS(app)

db.init_app(app)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api.add_resource( Property, '/property' )
api.add_resource(SpecificProperty, '/property/<int:id>')