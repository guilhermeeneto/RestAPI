from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

db_path = os.path.join(os.path.dirname(__file__), 'DB', 'futebol.db')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Clube(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    localizacao = db.Column(db.String(100))
    jogadores = db.relationship('Jogador', backref='clube', lazy=True)

class Jogador(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    idade = db.Column(db.Integer)
    posicao = db.Column(db.String(100))
    clube_id = db.Column(db.Integer, db.ForeignKey('clube.id'), nullable=False)

@app.route('/clubes', methods=['GET'])
def get_clubes():
    clubes = Clube.query.all()
    return jsonify([{'id': c.id, 'nome': c.nome, 'localizacao': c.localizacao} for c in clubes])

@app.route('/jogadores', methods=['GET'])
def get_jogadores():
    jogadores = Jogador.query.all()
    return jsonify([{'id': j.id, 'nome': j.nome, 'idade': j.idade, 'posicao': j.posicao, 'clube_id': j.clube_id} for j in jogadores])

@app.route('/clube', methods=['POST'])
def add_clube():
    data = request.get_json()
    novo_clube = Clube(nome=data['nome'], localizacao=data.get('localizacao'))
    db.session.add(novo_clube)
    db.session.commit()
    return jsonify({'id': novo_clube.id}), 201

@app.route('/jogador', methods=['POST'])
def add_jogador():
    data = request.get_json()
    novo_jogador = Jogador(nome=data['nome'], idade=data['idade'], posicao=data['posicao'], clube_id=data['clube_id'])
    db.session.add(novo_jogador)
    db.session.commit()
    return jsonify({'id': novo_jogador.id}), 201

if __name__ == '__main__':
    with app.app_context():
        db.create_all() 
    app.run(debug=True)
