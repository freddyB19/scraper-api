from fastapi import FastAPI

from fastapi_pagination import add_pagination

from routes.api.router import router
from routes.graphql.schemas import graphql_app

app = FastAPI()

app.include_router(router)
app.include_router(graphql_app, prefix = "/graphql")

add_pagination(app)
