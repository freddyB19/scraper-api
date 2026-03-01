import strawberry
from strawberry.fastapi import GraphQLRouter

from .querys import Query

schema = strawberry.Schema(query = Query)

graphql_app = GraphQLRouter(schema)
