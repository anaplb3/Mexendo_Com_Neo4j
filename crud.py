from flask import Flask, jsonify
from py2neo import Graph
from banco import Dao

app = Flask(__name__)
graph = Graph("bolt://localhost:7687", auth=("neo4j", "anaehtop"))


dao = Dao()
result = dao.listando_todos()

print(result)

print(dao.listando_por_nome("Juan"))

@app.route('/')
def olar():
   return "b"




app.run()

