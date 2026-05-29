from flask import Blueprint
from flask import request
from flask import jsonify

from app.database.connection import db
from app.models.usuario import Usuario

usuarios_bp = Blueprint(
    'usuarios',
    __name__
)

# LISTAR
@usuarios_bp.route('/usuarios', methods=['GET'])
def listar_usuarios():

    usuarios = Usuario.query.all()

    return jsonify([
        usuario.to_dict()
        for usuario in usuarios
    ])


# CRIAR
@usuarios_bp.route('/usuarios', methods=['POST'])
def criar_usuario():

    dados = request.json

    usuario = Usuario(
        nome=dados['nome'],
        email=dados['email']
    )

    db.session.add(usuario)
    db.session.commit()

    return jsonify(
        usuario.to_dict()
    ), 201