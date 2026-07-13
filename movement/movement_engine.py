from PySide6.QtCore import QObject, QPoint, QTimer, Signal


class MovementEngine(QObject):
    """
    Smoothly moves the pet from one position to another.
    """

    position_changed = Signal(QPoint)
    movement_finished = Signal()

    def __init__(self):
        super().__init__()

        self.current = QPoint()
        self.target = QPoint()

        self.speed = 4  # pixels per update

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_position)

    def move_to(self, start: QPoint, target: QPoint):

        self.current = QPoint(start)
        self.target = QPoint(target)

        self.timer.start(16)  # ~60 FPS

    def update_position(self):

        dx = self.target.x() - self.current.x()
        dy = self.target.y() - self.current.y()

        if abs(dx) <= self.speed and abs(dy) <= self.speed:

            self.current = QPoint(self.target)

            self.position_changed.emit(self.current)

            self.timer.stop()

            self.movement_finished.emit()

            return

        if dx:
            self.current.setX(
                self.current.x() + self.speed * (1 if dx > 0 else -1)
            )

        if dy:
            self.current.setY(
                self.current.y() + self.speed * (1 if dy > 0 else -1)
            )

        self.position_changed.emit(self.current)