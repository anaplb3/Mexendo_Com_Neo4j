from py2neo import Graph
import json


class Dao:
    def __init__(self):
        self.graph = Graph("bolt://localhost:7687", auth=("neo4j", "tcctcc"))

    def get_licitacoes(self, num_resultados):
        result = self.graph.run('match (x:Licitacao) return x limit {num}', num=num_resultados)
        nodes = [n for n in result]
        return nodes

    def get_participantes(self, num_resultados):
        result = self.graph.run('match (x:Participante) return x limit {num}', num=num_resultados)
        nodes = [n for n in result]
        return nodes

    def get_licitacao_nomeunidadegestora(self, nome):
        result = self.graph.run('match (lic:Licitacao{NomeUnidadeGest:$nome}) return lic', nome=nome)
        nodes = [n for n in result]
        return nodes

    def get_licitacao_por_ano(self, ano):
        result = self.graph.run('match (lic:Licitacao) WHERE lic.Data CONTAINS {ano} return lic', ano=ano)
        nodes = [n for n in result]
        return nodes

    # Busca participante pelo cpf ou cnpj
    def get_participante_por_codigo(self, codigo):
        result = self.graph.run("match (part:Participante{ChaveParticipante:$codigo}) return part", codigo=codigo)
        nodes = [n for n in result]
        return nodes

