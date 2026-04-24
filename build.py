"""Build a double-clickable executable of Link's Dungeon for the OS this runs on.

    uv run --group build build.py      -> dist/LinksDungeon.exe (Windows) or dist/LinksDungeon

uv sets up .venv with the Python from .python-version, pygame and PyInstaller
(see pyproject.toml), then this script bundles the game and assets/ into one file.
PyInstaller cannot cross-compile: run this on each OS you need.
"""
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))

try:
    import PyInstaller  # noqa: F401  (installed by the "build" dependency group)
except ImportError:
    sys.exit("PyInstaller is missing. Run:  uv run --group build build.py")

work = os.path.join(ROOT, "build")
subprocess.check_call([
    sys.executable, "-m", "PyInstaller", "--noconfirm", "--clean", "--onefile",
    "--name", "LinksDungeon",
    # keep the console: the game prints its rules and controls there
    "--add-data", os.path.join(ROOT, "assets") + os.pathsep + "assets",
    "--distpath", os.path.join(ROOT, "dist"), "--workpath", work, "--specpath", work,
    os.path.join(ROOT, "main.py"),
])
exe = os.path.join(ROOT, "dist", "LinksDungeon" + (".exe" if os.name == "nt" else ""))
print(f"\nBuilt: {exe}")
