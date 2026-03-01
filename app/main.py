from fastapi import FastAPI

from routes.graphql.schemas import graphql_app

app = FastAPI()

app.include_router(graphql_app, prefix = "/graphql")
