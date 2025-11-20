import sys
from logging.config import dictConfig


def setup_logger() -> None:
    config = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "my_formatter": {"format": "%(asctime)s %(name)s (line %(lineno)s) | %(levelname)s %(message)s"}
        },
        "handlers": {
            "console_stderr": {
                "class": "logging.StreamHandler",
                "level": "ERROR",
                "formatter": "my_formatter",
                "stream": sys.stderr,
            },
            "console_stdout": {
                "class": "logging.StreamHandler",
                "level": "INFO",
                "formatter": "my_formatter",
                "stream": sys.stdout,
            },
        },
        "root": {
            # In general, this should be kept at 'NOTSET'.
            # Otherwise it would interfere with the log levels set for each handler.
            "level": "NOTSET",
            "handlers": ["console_stderr", "console_stdout"],
        },
    }
    dictConfig(config)
