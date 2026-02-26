from dishka import Provider
from dishka.integrations.fastapi import setup_dishka
from fastapi import FastAPI

from fizz_buzz.custom_logging import setup_logger
from fizz_buzz.setup.app_factory import (
    configure_app,
    create_app,
    create_async_ioc_container,
    create_ioc_container_context,
)
from fizz_buzz.setup.ioc.registry import get_providers


class AppCreator:
    def __init__(self, *di_providers: Provider) -> None:
        self.app = create_app()
        configure_app(app=self.app)

        async_ioc_container = create_async_ioc_container(
            providers=(*get_providers(), *di_providers),
            context=create_ioc_container_context(),
        )
        setup_dishka(container=async_ioc_container, app=self.app)
        setup_logger()

        @self.app.get("/")
        def root():
            return "Test: service is working"


def create_app_instance() -> FastAPI:
    return AppCreator().app
