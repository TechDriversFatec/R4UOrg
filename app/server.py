import ia_fuzzy
import os
import schedule
import time
import random
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

filmes = { "1": [], "2": [], "3": [], "4": [], "5": [], "6": [], "7": [], "8": [], "9": [] }

def job():
    filmes[str(i)].append(ia_fuzzy.getFilmeByGrupo(str(i)))

i = 1
schedule.every(10).minutes.do(job(i))
i+=1
if(i==10): i = 1

# Rota mockada sem processamento da IA para envio do filme.
@app.route('/getFilme/<string:id>', methods=['GET'])
def getFilme(id):
    return jsonify({"filme": "Avengers: Endgame"})

# Rota com processamento da IA para envio do filme.
@app.route('/getFilmeIA/<string:id>', methods=['GET'])
def getFilmeIA(id):
    return jsonify({"filme": random.choice(filmes[id])})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=port)