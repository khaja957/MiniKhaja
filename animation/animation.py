from pathlib import Path
from PySide6.QtGui import QPixmap


class Animation:

    def __init__(self, folder, fps=30, loop=True):

        self.folder = Path(folder)
        self.fps = fps
        self.loop = loop

        self.frames = []

        self.load()

    def load(self):

        files = sorted(self.folder.glob("*.png"))

        for file in files:
            self.frames.append(QPixmap(str(file)))

    @property
    def frame_count(self):

        return len(self.frames)