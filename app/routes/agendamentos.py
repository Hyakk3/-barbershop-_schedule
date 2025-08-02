from flask import Blueprint, render_template, redirect, url_for, flash
from app.forms import AgendamentoForm
from app import db
from app.models import Agendamento, Cliente
from datetime import datetime
from zoneinfo import ZoneInfo

agendamentos_bp = Blueprint('agendamentos', __name__, url_prefix='/agendamentos')

@agendamentos_bp.route("/novo", methods=["GET", "POST"])
def novo_agendamento():
    form = AgendamentoForm()

    form.cliente_id.choices = [(c.id, c.nome) for c in Cliente.query.all()]

    now_brasilia = datetime.now(ZoneInfo("America/Sao_Paulo"))
    now_for_input = now_brasilia.replace(tzinfo=None)
    min_inicio = now_for_input.strftime('%Y-%m-%dT%H:%M')


    if form.validate_on_submit():
        agendamento = Agendamento(
            cliente_id=form.cliente_id.data,
            inicio=form.inicio.data,
            fim=form.fim.data
        )
        db.session.add(agendamento)
        db.session.commit()
        return redirect(url_for("agendamentos.lista_agendamentos"))

    return render_template("agendamentos/novo_agendamento.html", form=form, min_inicio=min_inicio)

@agendamentos_bp.route("/")
def lista_agendamentos():
    agendamentos = Agendamento.query.all()
    return render_template("agendamentos/lista_agendamentos.html", agendamentos=agendamentos)


@agendamentos_bp.route("/finalizar/<int:id>")
def finalizar_agendamento(id):
    agendamento = Agendamento.query.get_or_404(id)
    agendamento.finalizado_em = datetime.now()
    db.session.commit()
    flash("Agendamento finalizado com sucesso!", "success")
    return redirect(url_for("agendamentos.lista_agendamentos"))

from flask import redirect, url_for, flash
from app.models import Agendamento
from app import db

@agendamentos_bp.route('/excluir/<int:id>', methods=['POST', 'GET'])
def excluir_agendamento(id):
    agendamento = Agendamento.query.get_or_404(id)
    db.session.delete(agendamento)
    db.session.commit()
    flash('Agendamento excluído com sucesso!', 'success')
    return redirect(url_for('agendamentos.lista_agendamentos'))

