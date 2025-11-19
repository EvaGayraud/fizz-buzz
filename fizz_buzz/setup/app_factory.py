__all__ = (
    "configure_app",
    "create_app",
    "create_async_ioc_container",
    "create_ioc_container_context"
)

from collections.abc import Iterable

from dishka import Provider, AsyncContainer, make_async_container
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from starlette.middleware.cors import CORSMiddleware

from fizz_buzz.infrastructure.exceptions.handlers import setup_handlers
from fizz_buzz.setup.settings.core import Settings, CoreSettings
from fizz_buzz.infrastructure.api.v1 import routes as v1_api

def create_app() -> FastAPI:
    return FastAPI(title=Settings().PROJECT_NAME, default_response_class=ORJSONResponse)


def configure_app(
    app: FastAPI,
) -> None:
    app.add_middleware(
        CORSMiddleware,
        allow_origin_regex=Settings().CORS_ALLOW_ORIGIN_REGEX,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.include_router(v1_api.router, prefix=Settings().API_V1_STR)
    setup_handlers(app)


def create_async_ioc_container(
    providers: Iterable[Provider],
    context: dict,
) -> AsyncContainer:
    return make_async_container(*providers, context=context)


def create_ioc_container_context() -> dict:
    return {CoreSettings: CoreSettings()}
