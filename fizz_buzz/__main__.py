from fizz_buzz.app_creator import AppCreator
from fizz_buzz.custom_logging import setup_logger

app_creator = AppCreator()
app = app_creator.app

if __name__ == "__main__":
    import uvicorn

    setup_logger()

    uvicorn_kwargs = dict(
        app="fizz_buzz.app_creator:create_app_instance",
        port=8000,
        workers=1,
        proxy_headers=True,
        host="0.0.0.0",
        loop="uvloop",
        factory=True,
    )
    uvicorn.run(**uvicorn_kwargs)
