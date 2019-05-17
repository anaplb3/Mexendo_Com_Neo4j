from flask import Flask, jsonify
from py2neo import Graph
from banco import Dao

app = Flask(__name__)
dao = Dao()

@app.route('/')
def olar():
    return "inicio"


@app.route('/licitacoes')
def get_json_licitacoes():
   result = dao.get_licitacoes(2)
   return jsonify(result)

@app.route('/participantes')
def get_json_participantes():
   result = dao.get_participantes(2)
   return jsonify(result)

#print(dao.get_licitacao_nomeunidadegestora("Câmara Municipal de Alcantil"))

app.run(debug=True)
