from src.model.aluno import Aluno
from src.app.server import app
from src.controllers.alunoController import AlunoController
from src.controllers.response import Answer
from flask import request


@app.route("/")
def index():
    return "Hello Jillian!!"


@app.route("/aluno/", methods=["GET"])
def get_aluno():
    dados = AlunoController.get(Aluno)
    return Answer.newResponse(200, dados, "Sucesso")


@app.route("/aluno/<id>", methods=["GET"])
def get_aluno_id(id):
    dados = AlunoController.get_id(id)
    return Answer.newResponse(200, dados, "Sucesso")


@app.route("/aluno/", methods=["POST"])
def create_aluno():
    body = request.get_json()
    dados = AlunoController.create(body)
    return Answer.newResponse(dados["status"], dados["conteudo"], dados["mensagem"])


@app.route("/aluno/<id>", methods=["PUT"])
def update_aluno(id):
    body = request.get_json()
    dados = AlunoController.update(id, body)
    return Answer.newResponse(dados["status"], dados["conteudo"], dados["mensagem"])


@app.route("/aluno/<id>", methods=["DELETE"])
def delete_aluno(id):
    dados = AlunoController.delete(id)
    return Answer.newResponse(dados["status"], dados["conteudo"], dados["mensagem"])


# if __name__ == "__main__":
#     app.run()
