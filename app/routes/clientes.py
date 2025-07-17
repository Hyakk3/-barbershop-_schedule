from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models import Cliente

clientes_bp = Blueprint('clientes', __name__, template_folder='../templates/clientes')

@clientes_bp.route('/')
def listar_clientes():
    clientes = Cliente.query.all()
    return render_template('clientes/listar.html', clientes=clientes)

@clientes_bp.route('/novo', methods=['GET', 'POST'])
def novo_cliente():
    if request.method == 'POST':
        nome = request.form['nome']
        telefone = request.form['telefone']
        cliente = Cliente(nome=nome, telefone=telefone)
        db.session.add(cliente)
        db.session.commit()
        return redirect(url_for('clientes.listar_clientes'))
    return render_template('clientes/form.html')
