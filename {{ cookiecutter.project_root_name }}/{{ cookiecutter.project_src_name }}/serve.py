#!/usr/bin/env python
import os

import uvicorn
from esmerald.conf import settings

from .main import app as app  # no qa

if __name__ == "__main__":
    """
    Sets a default `FLUIDAPI_SETTINGS_MODULE` settings configuration and loads accordingly.
    """
    port = getattr(settings, "port", 8001)
    uvicorn.run(
        "main:app",
        debug=os.getenv("DEBUG", settings.debug),
        port=os.getenv("PORT", port),
        host=os.getenv("HOST", "localhost"),
        reload=True,
        lifespan="on",
        log_level="debug",
    )
