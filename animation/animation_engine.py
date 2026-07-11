from PySide6.QtCore import QObject, QTimer, Signal

from core.config import DEFAULT_FPS


class AnimationEngine(QObject):

    frame_changed = Signal(object)

    def __init__(self):

        super().__init__()

        self.frames = []

        self.current_index = 0

        self.timer = QTimer()

        self.timer.timeout.connect(self.next_frame)

    def play(self, frames, fps=DEFAULT_FPS):

        self.frames = frames

        self.current_index = 0

        if self.frames:
            self.frame_changed.emit(self.frames[0])

        self.timer.start(1000 // fps)

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