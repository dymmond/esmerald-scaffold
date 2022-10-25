import os
import sys
from pathlib import Path

from esmerald import Esmerald
from esmerald.routing.router import Include


def build_path():
    """
    Builds the path of the project and project root.
    """
    Path(__file__).resolve().parent.parent
    SITE_ROOT = os.path.dirname(os.path.realpath(__file__))

    if not SITE_ROOT in sys.path:
        sys.path.append(SITE_ROOT)
        sys.path.append(os.path.join(SITE_ROOT, "apps"))


def get_application():
    """
    This is optional. The function is only used for organisation purposes.
    """
    build_path()

    app = Esmerald(
        routes=[Include(namespace="{{ cookiecutter.project_src_name }}.urls")],
    )
    return app


app = get_application()
