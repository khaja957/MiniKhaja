from pathlib import Path

from PySide6.QtGui import QPixmap

from core.config import SPRITES_DIR


class SpriteLoader:
    """
    Loads animation frames from disk.
    """

    def load(self, animation_name: str) -> list[QPixmap]:

        folder = SPRITES_DIR / animation_name

        if not folder.exists():
            raise FileNotFoundError(folder)

        frames = []

        for image in sorted(folder.glob("*.png")):
            frames.append(QPixmap(str(image)))

        return frames