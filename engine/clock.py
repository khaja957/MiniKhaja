from PySide6.QtCore import QElapsedTimer


class GameClock:

    def __init__(self):

        self.timer = QElapsedTimer()

        self.timer.start()

    def delta(self):

        elapsed = self.timer.restart()

        return elapsed / 1000.0