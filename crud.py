from flask import Flask, jsonify
from py2neo import Graph
from banco import Dao

app = Flask(__name__)
#graph = Graph("bolt://localhost:7687", auth=("neo4j", "anaehtop"))
dao = Dao()

# print(result)

#print(dao.get_licitacao_nomeunidadegestora("Prefeitura Municipal de Santa In\u00eas"))


@app.route('/busca')
def olar():
    result = dao.get_participante_por_codigo("10578305000139")
    return jsonify(result)


@app.route("/ano")
def busca_ano():
   result = dao.get_licitacao_por_ano("2016")
   return jsonify(result)

@app.route('/lic')
def get_lic():
   result = dao.get_licitacoes()
   return jsonify(result)


app.run(debug=True)
