from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from app.models import Cliente
from app.forms import ClienteForm


clientes_bp = Blueprint('clientes', __name__, url_prefix='/clientes')

@clientes_bp.route('/novo', methods=['GET', 'POST'])
def novo_cliente():
    form = ClienteForm()
    if form.validate_on_submit():
        form.save()
        flash("Cliente cadastrado com sucesso!", "success")
        return redirect(url_for('clientes.lista_clientes'))
    elif request.method == 'POST':
        flash("Erro ao cadastrar cliente. Verifique os campos!", "error")
    return render_template('clientes/novo_cliente.html', form=form)


@clientes_bp.route("/")
def lista_clientes():
    clientes = Cliente.query.all()
    return render_template("clientes/lista_clientes.html", clientes=clientes)


@clientes_bp.route('/excluir/<int:id>', methods=['POST', 'GET'])
def excluir_cliente(id):
    cliente = Cliente.query.get_or_404(id)
    db.session.delete(cliente)
    db.session.commit()
    flash('Cliente excluído com sucesso!', 'success')
    return redirect(url_for('clientes.lista_clientes'))