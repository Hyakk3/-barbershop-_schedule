from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models import Agendamento, Cliente
from datetime import datetime

agendamentos_bp = Blueprint('agendamentos', __name__, template_folder='../templates/agendamentos')

@agendamentos_bp.route('/')
def listar_agendamentos():
    agendamentos = Agendamento.query.all()
    return render_template('agendamentos/listar.html', agendamentos=agendamentos)

@agendamentos_bp.route('/novo', methods=['GET', 'POST'])
def novo_agendamento():
    clientes = Cliente.query.all()
    if request.method == 'POST':
        cliente_id = request.form['cliente_id']
        inicio = datetime.strptime(request.form['inicio'], '%Y-%m-%dT%H:%M')
        fim = datetime.strptime(request.form['fim'], '%Y-%m-%dT%H:%M')
        agendamento = Agendamento(cliente_id=cliente_id, inicio=inicio, fim=fim)
        db.session.add(agendamento)
        db.session.commit()
        return redirect(url_for('agendamentos.listar_agendamentos'))
    return render_template('agendamentos/form.html', clientes=clientes)

@agendamentos_bp.route('/finalizar/<int:id>')
def finalizar_agendamento(id):
    agendamento = Agendamento.query.get_or_404(id)
    agendamento.finalizado_em = datetime.now()
    db.session.commit()
    return redirect(url_for('agendamentos.listar_agendamentos'))
