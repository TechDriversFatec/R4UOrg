import ia_fuzzy
import os
import random
from flask import Flask, jsonify, abort, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from threading import Thread

if (os.environ.get('ENV') != 'prod'):
    os.environ['DATABASE_URL'] = 'postgres://fatec:fatec@postgres:5432/pi'  

app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)
migrate = Migrate(app, db)
port = int(os.environ.get("PORT", 5000))

class Filme(db.Model):
    id = db.Column(db.Integer, db.Sequence('seq'), primary_key=True)
    grupo = db.Column(db.String(1))
    nome = db.Column(db.String(200))

    def __init__(self, grupo, nome):
        self.grupo = grupo
        self.nome = nome

    def serialize(self):
        return {
            "id": self.id,
            "grupo": self.grupo,
            "name": self.nome
        }

filmes = { "1": [], "2": [], "3": [], "4": [], "5": [], "6": [], "7": [], "8": [], "9": [] }

@app.route('/getFilmes', methods=['GET'])
def getFilmes():
    return jsonify({'filmes': list(map(lambda filme: filme.serialize(), Filme.query.all()))})

@app.route('/getFilmes/<int:grupo>', methods=['GET'])
def getFilmesByGrupo(grupo):
    return jsonify({'filmes': list(map(lambda filme: filme.serialize(), Filme.query.filter_by(grupo=str(grupo)).all()))})

# Rota mockada sem processamento da IA para envio do filme.
@app.route('/getFilme/<int:grupo>', methods=['GET'])
def getFilme(grupo):
    return jsonify({"filme": "Avengers: Endgame"})

# Rota com processamento da IA para envio do filme.
@app.route('/getFilmeIA/<int:grupo>', methods=['GET'])
def getFilmeIA(grupo):
    if(grupo>0 and grupo<10):
        return jsonify({"filme": "teste"})
    else:
        return jsonify({"Erro": "Número de grupo inválido."})

@app.route('/getFilme/<string:grupo>', methods=['GET'])
def getFilmeString(grupo):
    return jsonify({"Erro": "Envie um número."})

def buscaFilme(grupo):
    filme = Filme(grupo, ia_fuzzy.getFilmeByGrupo(grupo))
    db.session.add(filme)
    db.session.commit()
    buscaFilme(grupo)

if __name__ == '__main__':
    for grupo in range(1,10):
        thread = Thread(target=buscaFilme, args=(str(grupo),))
        thread.start()
    app.run(debug=True, host='0.0.0.0', port=port)