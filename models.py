from py2neo.ogm import GraphObject, Property
from neo4j import GraphDatabase

driver = GraphDatabase.driver("bolt//localhost:7687", auth=("neo4j", "anaehtop"))

class Pessoa(GraphObject):
    __primarykey__ = 'name'

    name = Property()
    idade = Property()

    def as_dict(self):
        return {
            'name': self.name,
            'idade': self.idade
        }

    def fetch(self):
        return self.select(driver, self.name).first()

