from . import db

class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    telefone = db.Column(db.String(20), nullable=False)

    agendamentos = db.relationship('Agendamento', backref='cliente', lazy=True)

class Agendamento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'), nullable=False)
    inicio = db.Column(db.DateTime, nullable=False)
    fim = db.Column(db.DateTime, nullable=False)
    finalizado_em = db.Column(db.DateTime, nullable=True)

    def disponibilidade_restante(self):
        if self.finalizado_em:
            return self.fim - self.finalizado_em
        return None
