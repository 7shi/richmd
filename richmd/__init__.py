"""richmd - Markdown viewer using rich library."""
from importlib.metadata import version

__version__ = version("richmd")
__license__ = "CC0-1.0"

from .richmd import main

__all__ = ["main"]
