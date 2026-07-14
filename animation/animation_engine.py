from PySide6.QtCore import QObject, Signal, QTimer


class AnimationEngine(QObject):

    # Emits the current frame (QPixmap)
    frame_changed = Signal(object)
    animation_finished = Signal()

    def __init__(self):
        super().__init__()

        self.frames = []
        self.current_frame = 0

        self.loop = True
        self.fps = 12

        self.timer = QTimer()
        self.timer.timeout.connect(self.next_frame)

    # -------------------------------
    # Start playing an animation
    # -------------------------------
    def play(self, frames, loop=True, fps=12):

        if not frames:
            return

        self.frames = frames
        self.loop = loop
        self.fps = fps

        self.current_frame = 0

        # Show first frame immediately
        self.frame_changed.emit(self.frames[0])

        interval = int(1000 / self.fps)

        self.timer.start(interval)

    # -------------------------------
    # Stop animation
    # -------------------------------
    def stop(self):

        self.timer.stop()

    # -------------------------------
    # Advance to next frame
    # -------------------------------
    def next_frame(self):

        if not self.frames:
            return

        self.current_frame += 1

        # Reached the end?
        if self.current_frame >= len(self.frames):

            if self.loop:
                self.current_frame = 0

            else:
                self.stop()
                self.animation_finished.emit()
                return

        self.frame_changed.emit(
            self.frames[self.current_frame]
        )