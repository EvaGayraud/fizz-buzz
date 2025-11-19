from via_report_generator.setup.custom_logging import setup_logger

if __name__ == "__main__":
    import uvicorn

    setup_logger()

    uvicorn_kwargs = dict(
        app="via_report_generator.app_creator:create_app_instance",
        port=8080,
        workers=1,
        proxy_headers=True,
        host="0.0.0.0",
        loop="uvloop",
        factory=True,
    )
    uvicorn.run(**uvicorn_kwargs)
