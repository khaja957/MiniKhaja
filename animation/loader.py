import json
from pathlib import Path

from PySide6.QtGui import QPixmap

from animation.animation import Animation


class AnimationLoader:

    def __init__(self, asset_root: Path):

        self.asset_root = asset_root

    def load(self, animation_name: str) -> Animation:

        folder = self.asset_root / animation_name

        metadata_file = folder / "metadata.json"

        with open(metadata_file, "r") as f:

            metadata = json.load(f)

        frames = []

        for filename in metadata["frames"]:

            pixmap = QPixmap(str(folder / filename))

            frames.append(pixmap)

        return Animation(

            name=metadata["name"],

            fps=metadata["fps"],

            frames=frames,

            frame_count=len(frames),

            width=metadata["canvas"]["width"],

            height=metadata["canvas"]["height"]

        )