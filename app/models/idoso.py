from app.database.connection import db

class Idoso(db.Model):

    __tablename__ = 'idosos'

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    nome = db.Column(
        db.String(100),
        nullable=False
    )

    idade = db.Column(
        db.Integer,
        nullable=False
    )

    usuario_id = db.Column(
        db.Integer,
        db.ForeignKey('usuarios.id'),
        nullable=False
    )

    def to_dict(self):

        return {
            'id': self.id,
            'nome': self.nome,
            'idade': self.idade,
            'usuario_id': self.usuario_id
        }