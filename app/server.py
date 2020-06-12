import ia_fuzzy
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

# Rota mockada sem processamento da IA para envio do filme.
@app.route('/getFilme/<string:id>', methods=['GET'])
def getFilme(id):
    return jsonify({"filme": "Avengers: Endgame"})

# Rota com processamento da IA para envio do filme.
@app.route('/getFilmeIA/<string:id>', methods=['GET'])
def getFilmeIA(id):
    return jsonify({"filme": ia_fuzzy.getFilmeByGrupo(id)})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=port)