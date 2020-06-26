import ia_fuzzy
import os
import random
from flask import Flask, jsonify, abort, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from threading import Thread
from flask_swagger_ui import get_swaggerui_blueprint

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
            "nome": self.nome
        }
    
    def getNome(self):
        return self.nome

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

SWAGGER_URL =  '/swagger'
API_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Topicos Avançados"
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

# Rota que retorna todos os filmes cadastrados no banco.
@app.route('/getFilmes', methods=['GET'])
def getFilmes():
    return jsonify({'filmes': list(map(lambda filme: filme.serialize(), Filme.query.all()))})

# Rota que retorna todos os nomes dos filmes cadastrados por grupo.
@app.route('/getFilmes/<int:grupo>', methods=['GET'])
def getFilmesByGrupo(grupo):
    return jsonify({'filmes': sorted(list(map(lambda filme: filme.getNome(), Filme.query.filter_by(grupo=str(grupo)).all())))})

# Rota que retorna o nome de um filme recomendado por grupo.
@app.route('/getFilme/<int:grupo>', methods=['GET'])
def getFilme(grupo):
    if(grupo>0 and grupo<10):
        filmesByGrupo = list(map(lambda filme: filme.getNome(), Filme.query.filter_by(grupo=str(grupo)).all()))
        return jsonify({"filme": filmesByGrupo and random.choice(filmesByGrupo) or ""})
    else:
        return jsonify({"Erro": "Número de grupo inválido, envie um número de 1 a 9."}), 400

# Rota que retorna um erro caso seja enviado uma string invés de um número.
@app.route('/getFilme/<string:grupo>', methods=['GET'])
def getFilmeString(grupo):
    return jsonify({"Erro": "Envie um número de 1 a 9."}), 400

def getFilmeByGrupo(grupo):
    filmesByGrupo = list(map(lambda filme: filme.getNome(), Filme.query.filter_by(grupo=grupo).all()))
    if(len(filmesByGrupo)>15): return
    nome = ia_fuzzy.getFilmeByGrupo(grupo, filmesByGrupo)
    filmesByGrupo = list(map(lambda filme: filme.getNome(), Filme.query.filter_by(grupo=grupo).all()))
    if(nome not in filmesByGrupo):
        filme = Filme(grupo, nome)
        db.session.add(filme)
        db.session.commit()
    getFilmeByGrupo(grupo)

if __name__ == '__main__':
    for grupo in range(1,10):
        thread = Thread(target=getFilmeByGrupo, args=(str(grupo), ))
        thread.start()
    app.run(debug=True, host='0.0.0.0', port=port)