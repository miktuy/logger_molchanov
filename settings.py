import logging


class NewFunctionFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> int:
        return hasattr(record, "mike_name")


class MegaHandler(logging.Handler):
    def __init__(self, filename):
        super().__init__()
        self.filename = filename

    def emit(self, record: logging.LogRecord) -> None:
        msg = self.format(record)
        with open(self.filename, "a") as f:
            f.write(msg + "\n")



logger_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "std_format": {
            "format": "{asctime} - {levelname} - {name} - {module}:{funcName}:{lineno}- {message}",
            "style": "{",
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "std_format",
            # "filters": ["new_filter"],
        },
        "file": {
            "()": MegaHandler,
            "level": "DEBUG",
            "filename": "debug.log",
            "formatter": "std_format",
        }
    },
    "loggers": {
        "app_logger": {
            "level": "DEBUG",
            "handlers": ["console", "file"]
            # "propagate": False
        }
    },
    "filters": {
        "new_filter": {
            "()": NewFunctionFilter,
        }
    },
    # "": {}
    # "incremental": True
}
