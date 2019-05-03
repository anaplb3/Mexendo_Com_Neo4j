from flask import Flask, jsonify
from py2neo import Graph
from banco import Dao

app = Flask(__name__)
#graph = Graph("bolt://localhost:7687", auth=("neo4j", "anaehtop"))
dao = Dao()

# print(result)

print(dao.get_licitacao_nomeunidadegestora("Prefeitura Municipal de Santa In\u00eas"))


@app.route('/ooo')
def olar():
    return "b"


@app.route('/lic')
def get_lic():
   result = dao.get_licitacao()
   return jsonify(result)


app.run(debug=True)
