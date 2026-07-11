from pathlib import Path

from PySide6.QtCore import QObject, QTimer, Signal
from PySide6.QtGui import QPixmap


class AnimationPlayer(QObject):
    """
    Handles animation playback.
    """

    frame_changed = Signal(QPixmap)

    def __init__(self):
        super().__init__()

        self.frames = []
        self.current_index = 0

        self.timer = QTimer()

        self.timer.timeout.connect(self.next_frame)

    def load(self, folder: Path):

        self.stop()

        self.frames.clear()

        for file in sorted(folder.glob("*.png")):
            self.frames.append(QPixmap(str(file)))

        self.current_index = 0

        if self.frames:
            self.frame_changed.emit(self.frames[0])

    def play(self, fps=6):

        if len(self.frames) < 2:
            return

        self.timer.start(int(1000 / fps))

    def stop(self):

        self.timer.stop()

    def next_frame(self):

        if not self.frames:
            return

        self.current_index += 1
        self.current_index %= len(self.frames)

        self.frame_changed.emit(
            self.frames[self.current_index]
        )