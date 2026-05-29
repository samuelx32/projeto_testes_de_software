from flask import Flask
from flask_cors import CORS
from app.models.idoso import Idoso
from app.models.responsavel import Responsavel
from app.database.connection import db
from app.routes.usuario import usuarios_bp

from app.routes.idosos import idosos_bp
from app.routes.responsaveis import responsaveis_bp

def create_app():

    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    CORS(app)

    db.init_app(app)

   
    app.register_blueprint(usuarios_bp)
    app.register_blueprint(idosos_bp)
    app.register_blueprint(responsaveis_bp)

    with app.app_context():
        db.create_all()

    return app