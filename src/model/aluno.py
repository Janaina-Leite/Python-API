from src.app.server import db


class Aluno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45))
    curso = db.Column(db.String(45))
    nota = db.Column(db.Float)

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "curso": self.curso,
            "nota": self.nota
        }
