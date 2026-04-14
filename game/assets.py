"""Find asset files relative to the program, not the current working directory.

From source, assets live in <repo>/assets. In a PyInstaller build they are unpacked
under sys._MEIPASS/assets, so the same lookup works for the packaged executable.
"""
import os
import sys

_ROOT = getattr(sys, "_MEIPASS", os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ASSET_DIR = os.path.join(_ROOT, "assets")


def asset_path(name):
    """Full path of an image in the assets folder, e.g. asset_path("floor.png")."""
    return os.path.join(ASSET_DIR, name)
