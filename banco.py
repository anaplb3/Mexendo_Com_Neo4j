from py2neo import Graph
import json

class Dao:
    def __init__(self):
        self.graph = Graph("bolt://localhost:7687", auth=("neo4j", "anaehtop"))

    def listando_todos(self):
        result = self.graph.run('match (x:Person) return x')
        nodes = [n for n in result]
        return json.dumps(nodes)

    def listando_por_nome(self, nome):
        return json.dumps(self.graph.nodes.match("Person", Name = nome).first())


