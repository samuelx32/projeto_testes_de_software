from flask import Blueprint
from flask import request
from flask import jsonify

from app.database.connection import db
from app.models.responsavel import Responsavel

responsaveis_bp = Blueprint(
    'responsaveis',
    __name__
)

# LISTAR
@responsaveis_bp.route('/responsaveis', methods=['GET'])
def listar_responsaveis():

    responsaveis = Responsavel.query.all()

    return jsonify([
        responsavel.to_dict()
        for responsavel in responsaveis
    ])


# CRIAR
@responsaveis_bp.route('/responsaveis', methods=['POST'])
def criar_responsavel():

    dados = request.json

    responsavel = Responsavel(
        nome=dados['nome'],
        telefone=dados['telefone'],
        idoso_id=dados['idoso_id']
    )

    db.session.add(responsavel)
    db.session.commit()

    return jsonify(
        responsavel.to_dict()
    ), 201