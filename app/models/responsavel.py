from app.database.connection import db

class Responsavel(db.Model):

    __tablename__ = 'responsaveis'

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    nome = db.Column(
        db.String(100),
        nullable=False
    )

    telefone = db.Column(
        db.String(30),
        nullable=False
    )

    idoso_id = db.Column(
        db.Integer,
        db.ForeignKey('idosos.id'),
        nullable=False
    )

    def to_dict(self):

        return {
            'id': self.id,
            'nome': self.nome,
            'telefone': self.telefone,
            'idoso_id': self.idoso_id
        }