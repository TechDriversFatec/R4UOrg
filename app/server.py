import os
from flask import Flask, jsonify, abort, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


if (os.environ.get('ENV') != 'prod'):
    os.environ['DATABASE_URL'] = 'postgres://fatec:fatec@postgres:5432/pi'  

app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)
migrate = Migrate(app, db)
port = int(os.environ.get("PORT", 5000))

# Exemplo de modelo para o banco de dados.
'''
class Developer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))

    def __init__(self, name):
        self.name = name

    def serialize(self):
        return {"id": self.id,
                "name": self.name}
'''

# Rota principal para envio do filme.
@app.route('/getFilme/<int:id>', methods=['GET'])
def getFilme(id):
    return jsonify({"filme": "Avengers: Endgame"})

# Exemplo de outras rotas que acessam o banco de dados.
'''
@app.route('/getFilme/<int:id>', methods=['GET'])
def getFilme(id):
    return jsonify({"filme": id})

@app.route('/dev/', methods=['GET'])
def index():
    return jsonify({'developers': list(map(lambda dev: dev.serialize(), Developer.query.all()))})

@app.route('/dev/<int:id>/')
def get_dev(id):
    return jsonify({'developer': Developer.query.get(id).serialize()})

@app.route('/dev/', methods=['POST'])
def create_dev():
    if not request.json or not 'name' in request.json:
        abort(400)
    dev = Developer(request.json['name'])
    db.session.add(dev)
    db.session.commit()
    return jsonify({'developer': dev.serialize()}), 201

@app.route('/dev/<int:id>/', methods=['DELETE'])
def delete_dev(id):
    db.session.delete(Developer.query.get(id))
    db.session.commit()
    return jsonify({'result': True})

@app.route('/dev/<int:id>/', methods=['PUT'])
def update_dev(id):
    dev = Developer.query.get(id)
    dev.name = request.json.get('name', dev.name)
    db.session.commit()
    return jsonify({'dev': dev.serialize()})
'''

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=port)