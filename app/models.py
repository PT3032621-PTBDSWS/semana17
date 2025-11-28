from . import db

class Curso(db.Model):
    __tablename__ = 'cursos'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(200), nullable=False)
    descricao = db.Column(db.String(300))

    def __repr__(self):
        return f'<Curso {self.nome}>'
