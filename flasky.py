from app import create_app, db
from app.models import User, Curso

app = create_app()

# Shell context for flask shell (optional)
@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Curso=Curso)
