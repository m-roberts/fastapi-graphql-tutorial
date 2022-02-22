import graphene
from fastapi import FastAPI
# from starlette.graphql import GraphQLApp
from starlette_graphene3 import GraphQLApp, make_graphiql_handler

from schema import Query, Mutation

app = FastAPI()

schema = graphene.Schema(query=Query, mutation=Mutation)

app.mount("/graphql", GraphQLApp(schema, on_get=make_graphiql_handler()))  # Graphiql IDE

@app.get('/')
def ping():
    return {'ping': 'pong'}
