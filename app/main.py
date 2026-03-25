from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from fastapi_pagination import add_pagination

from core.settings import config
from routes.api.router import router
from routes.graphql.schemas import graphql_app

app = FastAPI(
	docs_url="/docs",
    openapi_url="/openapi.json"
)

app.add_middleware(
	CORSMiddleware,
	allow_origins = config.cors_origins,
	allow_methods = ['GET', 'POST'],
	allow_headers = ['Content-Type'],
)

app.include_router(router)
app.include_router(graphql_app, prefix = "/graphql")

add_pagination(app)
