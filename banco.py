from py2neo import Graph
import json


class Dao:
    def __init__(self):
        self.graph = Graph("bolt://10.10.102.128:7687", auth=("neo4j", "tcctcc"))

    def get_licitacao(self):
        result = self.graph.run('match (x:Licitacao) return x')
        nodes = [n for n in result]
        return json.dumps(nodes)

    def get_participante(self):
        result = self.graph.run('match (x:Participante) return x')
        nodes = [n for n in result]
        return json.dumps(nodes)

    def get_licitacao_nomeunidadegestora(self, nome):
        return json.dumps(self.graph.nodes.match("Licitacao", NomeUnidadeGest = nome).first())

