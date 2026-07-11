from pathlib import Path

from PySide6.QtGui import QPixmap


class SpriteManager:
    """Loads sprites from disk."""

    def __init__(self):
        self.base_path = (
            Path("assets")
            / "sprites"
            / "character"
            / "idle"
        )

    def get_idle_sprite(self):
        sprite_path = self.base_path / "idle_01.png"

        return QPixmap(str(sprite_path))