from pathlib import Path

from PySide6.QtGui import QPixmap


class SpriteLoader:

    def __init__(self, asset_root):

        self.asset_root = Path(asset_root)

    def load_animation(self, animation_name):

        folder = self.asset_root / animation_name

        frames = []

        for file in sorted(folder.glob("*.png")):
            frames.append(QPixmap(str(file)))

        return frames