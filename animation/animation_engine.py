from PySide6.QtCore import QObject, QTimer, Signal


class AnimationEngine(QObject):

    frame_changed = Signal(object)

    def __init__(self):

        super().__init__()

        self.frames = []

        self.index = 0

        self.timer = QTimer()

        self.timer.timeout.connect(self.next_frame)

    def set_animation(self, frames, fps=8):

        self.frames = frames

        self.index = 0

        if frames:

            self.frame_changed.emit(frames[0])

        self.timer.start(1000 // fps)

    def next_frame(self):

        if not self.frames:
            return

        self.index = (self.index + 1) % len(self.frames)

        self.frame_changed.emit(
            self.frames[self.index]
        )