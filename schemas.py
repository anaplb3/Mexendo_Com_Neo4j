import graphene

class PessoaSchema(graphene.ObjectType):
    nome = graphene.String()
    idade = graphene.Int()