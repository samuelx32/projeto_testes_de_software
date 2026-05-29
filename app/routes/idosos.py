from flask import Blueprint
from flask import request
from flask import jsonify

from app.database.connection import db
from app.models.idoso import Idoso

idosos_bp = Blueprint(
    'idosos',
    __name__
)

# LISTAR
@idosos_bp.route('/idosos', methods=['GET'])
def listar_idosos():

    idosos = Idoso.query.all()

    return jsonify([
        idoso.to_dict()
        for idoso in idosos
    ])


# CRIAR
@idosos_bp.route('/idosos', methods=['POST'])
def criar_idoso():

    dados = request.json

    idoso = Idoso(
        nome=dados['nome'],
        idade=dados['idade'],
        usuario_id=dados['usuario_id']
    )

    db.session.add(idoso)
    db.session.commit()

    return jsonify(
        idoso.to_dict()
    ), 201