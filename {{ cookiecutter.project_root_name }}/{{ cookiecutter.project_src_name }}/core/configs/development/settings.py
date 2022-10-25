import logging
import sys
from typing import Any, List, Optional

from esmerald.conf.enums import EnvironmentType
from esmerald.conf.global_settings import EsmeraldAPISettings
from esmerald.logging import InterceptHandler
from esmerald.middleware.basic import BasicHTTPMiddleware
from esmerald.types import Middleware
from loguru import logger


class DevelopmentSettings(EsmeraldAPISettings):
    app_name: str = "My app in development mode"
    debug: bool = True
    environment: Optional[str] = EnvironmentType.DEVELOPMENT

    def __init__(self, *args: Any, **kwds: Any) -> Any:
        super().__init__(*args, **kwds)
        logging_level = logging.DEBUG if self.debug else logging.INFO
        loggers = ("uvicorn.asgi", "uvicorn.access", "esmerald")
        logging.getLogger().handlers = [InterceptHandler()]
        for logger_name in loggers:
            logging_logger = logging.getLogger(logger_name)
            logging_logger.handlers = [InterceptHandler(level=logging_level)]

        logger.configure(handlers=[{"sink": sys.stderr, "level": logging_level}])

    @property
    def middleware(self) -> List[Middleware]:
        """
        List of default middlewares of the application.
        """
        return [BasicHTTPMiddleware]
