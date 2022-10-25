from typing import List, Optional

from esmerald.conf.enums import EnvironmentType
from esmerald.conf.global_settings import EsmeraldAPISettings
from esmerald.middleware.basic import BasicHTTPMiddleware
from esmerald.types import Middleware


class TestingSettings(EsmeraldAPISettings):
    app_name: str = "My app in testing mode"
    debug: bool = True
    environment: Optional[str] = EnvironmentType.TESTING

    @property
    def middleware(self) -> List[Middleware]:
        """
        List of default middlewares of the application.
        """
        return [BasicHTTPMiddleware]
