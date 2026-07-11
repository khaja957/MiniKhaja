from pathlib import Path

# -----------------------
# Project Paths
# -----------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent

ASSETS_DIR = PROJECT_ROOT / "assets"

SPRITES_DIR = ASSETS_DIR / "sprites" / "character"

# -----------------------
# Window
# -----------------------

WINDOW_WIDTH = 220
WINDOW_HEIGHT = 220

# -----------------------
# Animation
# -----------------------

DEFAULT_FPS = 8

DEFAULT_STATE = "idle"