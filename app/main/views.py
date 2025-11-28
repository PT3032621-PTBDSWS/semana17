from flask import render_template, request, redirect, url_for, flash
from datetime import datetime
from . import bp
from app.models import Curso
from app import db

# ROTA PRINCIPAL
@bp.route('/')
def index():
    nome = "Fabio Teixeira"       # <-- coloque aqui seu nome
    prontuario = "PT23820X"       # <-- coloque aqui o seu prontuário

    data_hora = datetime.now().strftime("%B %d, %Y %I:%M %p")

    return render_template(
        'index.html',
        nome=nome,
        prontuario=prontuario,
        data_hora=data_hora
    )

# ROTA CURSOS
@bp.route('/cursos', methods=['GET', 'POST'])
def cursos():
    if request.method == 'POST':
        nome = request.form.get('nome')
        descricao = request.form.get('descricao')

        if not nome:
            flash("O nome do curso é obrigatório.")
            return redirect(url_for('main.cursos'))

        novo = Curso(nome=nome, descricao=descricao)
        db.session.add(novo)
        db.session.commit()

        return redirect(url_for('main.cursos'))

    lista = Curso.query.all()
    return render_template('cursos.html', cursos=lista)

# ROTAS NÃO IMPLEMENTADAS
@bp.route('/professores')
@bp.route('/disciplinas')
@bp.route('/alunos')
@bp.route('/ocorrencias')
def nao_disponivel():
    data_hora = datetime.now().strftime("%B %d, %Y %I:%M %p")
    return render_template('nao_disponivel.html', data_hora=data_hora)

# TRATAMENTO DE ERROS
def page_not_found(e):
    return render_template('404.html'), 404

def internal_error(e):
    return render_template('500.html'), 500
