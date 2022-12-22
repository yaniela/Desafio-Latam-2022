from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app import routes

#from app.routes import router
from config import AppConfig


def init_routers(app: FastAPI) -> None:
    app.include_router(routes.router)


def init_middlewares(app: FastAPI) -> None:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"])


def create_app() -> FastAPI:
    docs_url = None if AppConfig.ENV == "production" else "/docs"
    redoc_url = None if AppConfig.ENV == "production" else "/redoc"

    app = FastAPI(
        title="Desafio-Latam-API-models",
        description="API Services for desafio latam models",
        version="1.0.0",
        docs_url=docs_url,
        redoc_url=redoc_url,
    )
    init_routers(app)
    init_middlewares(app)
    return app


app = create_app()