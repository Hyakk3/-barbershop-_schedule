from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateTimeLocalField, SelectField, ValidationError
from wtforms.validators import DataRequired
from app.models import Cliente
from app import db
import re
from datetime import datetime

class ClienteForm(FlaskForm):
    nome = StringField("Nome", validators=[DataRequired()])
    telefone = StringField("Telefone", validators=[DataRequired()])
    submit = SubmitField("Salvar")

    def save(self):
        cliente = Cliente(nome=self.nome.data, telefone=self.telefone.data)
        db.session.add(cliente)
        db.session.commit()

    def validate_telefone(self, field):
        telefone = re.sub(r'\D', '', field.data)

        if len(telefone) not in (10, 11):
            raise ValidationError("Telefone deve conter 10 ou 11 dígitos numéricos (incluindo DDD).")
        field.data = telefone


class AgendamentoForm(FlaskForm):
    cliente_id = SelectField("Cliente", coerce=int, validators=[DataRequired()])
    inicio = DateTimeLocalField("Início", format="%Y-%m-%dT%H:%M", validators=[DataRequired()])
    fim = DateTimeLocalField("Fim", format="%Y-%m-%dT%H:%M", validators=[DataRequired()])
    submit = SubmitField("Salvar")

    def validate_inicio(self, field):
        agora = datetime.now()
        if field.data <= agora:
            raise ValidationError("A data/hora de início deve ser no futuro.")

    def validate_fim(self, field):
        if self.inicio.data and field.data <= self.inicio.data:
            raise ValidationError("A data/hora de fim deve ser após o início.")