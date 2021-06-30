from src.app.server import db
from src.model.aluno import Aluno


class AlunoController():

    def get(self):
        aluno = Aluno.query.all()
        dados = [Aluno.to_json() for Aluno in aluno]
        return dados

    def get_id(id):
        aluno = Aluno.query.filter_by(id=id).first()
        dados = aluno.to_json()
        return dados

    def create(body):
        try:
            aluno = Aluno(
                id=body["id"],
                name=body["name"],
                curso=body["curso"],
                nota=body["nota"]
            )
            db.session.add(aluno)
            db.session.commit()
            return {
                "status": 201,
                "conteudo": {},
                "mensagem": "Sucesso"
            }
        except Exception as e:
            return {
                "status": 400,
                "conteudo": {},
                "mensagem": "Erro"
            }

    def update(id, body):
        aluno = Aluno.query.filter_by(id=id).first()
        try:
            aluno.id = body["id"]
            aluno.name = body["name"]
            aluno.curso = body["curso"]
            aluno.nota = body["nota"]
            db.session.commit()
            return {
                "status": 201,
                "conteudo": {},
                "mensagem": "Sucesso"
            }
        except Exception as e:
            return {
                "status": 400,
                "conteudo": {},
                "mensagem": "Erro"
            }

    def delete(id):
        aluno = Aluno.query.filter_by(id=id).first()
        try:
            db.session.delete(aluno)
            db.session.commit()
            return {
                "status": 201,
                "conteudo": {},
                "mensagem": "Sucesso"
            }
        except Exception as e:
            return {
                "status": 400,
                "conteudo": {},
                "mensagem": "Erro"
            }
