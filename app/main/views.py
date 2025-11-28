from flask import render_template, request
from . import bp
from datetime import datetime
from ..models import Curso
from .. import db
from ..auth.forms import LoginForm
from flask import current_app

# ROTA PRINCIPAL — Avaliação semestral (mostra nome e prontuário)
@bp.route('/')
def index():
    # **substitua com seu nome e prontuário** antes da prova ou deixe dinâmico
    nome = "Seu Nome Aqui"
    prontuario = "PT123456X"
    data_hora = datetime.now().strftime("%B %d, %Y %I:%M %p")  # formato em inglês como no exemplo
    return render_template('index.html', nome=nome, prontuario=prontuario, data_hora=data_hora)

# ROTA DE CURSOS (GET = listar, POST = cadastrar)
@bp.route('/cursos', methods=['GET', 'POST'])
def cursos():
    from ..auth.forms import LoginForm  # só para manter import correto se necessário
    from ..auth.forms import LoginForm
    from flask import redirect, url_for, flash

    # formulário para cadastro de cursos (simples, sem WTForms aqui para reduzir dependências)
    if request.method == 'POST':
        nome = request.form.get('nome')
        descricao = request.form.get('descricao')
        if not nome:
            flash('Nome do curso é obrigatório.')
            return redirect(url_for('main.cursos'))
        curso = Curso(nome=nome, descricao=descricao)
        db.session.add(curso)
        db.session.commit()
        return redirect(url_for('main.cursos'))

    cursos = Curso.query.all()
    return render_template('cursos.html', cursos=cursos)

# ROTAS NÃO DISPONÍVEIS (devem retornar "Não disponível" + data/hora)
@bp.route('/professores')
@bp.route('/disciplinas')
@bp.route('/alunos')
@bp.route('/ocorrencias')
def nao_disponivel():
    data_hora = datetime.now().strftime("%B %d, %Y %I:%M %p")
    return render_template('nao_disponivel.html', data_hora=data_hora)
