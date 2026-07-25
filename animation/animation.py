from dataclasses import dataclass

from PySide6.QtGui import QPixmap


@dataclass
class Animation:

    name: str

    fps: float

    frames: list[QPixmap]

    frame_count: int

    width: int

    height: int