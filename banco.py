from py2neo import Graph
import json


class Dao:
    def __init__(self):
        self.graph = Graph("bolt://localhost:7687", auth=("neo4j", "tcctcc"))

    def get_licitacoes(self):
        result = self.graph.run('match (x:Licitacao) return x')
        nodes = [n for n in result]
        return json.dumps(nodes)

    def get_participantes(self):
        result = self.graph.run('match (x:Participante) return x')
        nodes = [n for n in result]
        return json.dumps(nodes)

    def get_licitacao_nomeunidadegestora(self, nome):
        result = self.graph.run('match (lic:Licitacao{NomeUnidadeGest:$nome}) return lic', nome=nome)
        nodes = [n for n in result]
        return json.dumps(nodes)
