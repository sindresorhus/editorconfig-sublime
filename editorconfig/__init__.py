"""EditorConfig Python Core"""

from .versiontools import join_version

VERSION = (0, 12, 2, "final")

__all__ = ['get_properties', 'EditorConfigError', 'exceptions']

__version__ = join_version(VERSION)


def get_properties(filename):
    """Locate and parse EditorConfig files for the given filename"""
    handler = EditorConfigHandler(filename)
    return handler.get_configurations()


from .handler import EditorConfigHandler
from .exceptions import *
