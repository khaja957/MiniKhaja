import sys

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication

from ui.window import CompanionWindow
from animation.player import AnimationPlayer
from companion.companion import Companion
from engine.clock import GameClock


class MiniKhajaApplication:

    def __init__(self):

        self.qt_app = QApplication(sys.argv)

        # Window
        self.window = CompanionWindow()

        # Animation Renderer
        self.player = AnimationPlayer(self.window)

        # Companion Runtime
        self.companion = Companion(self.player)

        # Game Clock
        self.clock = GameClock()

        # Main Update Timer (~60 FPS)
        self.timer = QTimer()
        self.timer.setInterval(16)
        self.timer.timeout.connect(self.update)

    def start(self):

        print("=" * 50)
        print("MiniKhaja Runtime Starting...")
        print("=" * 50)

        # Load companion assets
        self.companion.load()

        # Initial State
        self.companion.start()

        # Show Window
        self.window.show()

        # Start Runtime Loop
        self.timer.start()

        print("Runtime Started Successfully.")
        print()

        return self.qt_app.exec()

    def update(self):

        dt = self.clock.delta()

        self.companion.update(dt)


def main():

    runtime = MiniKhajaApplication()

    sys.exit(runtime.start())


if __name__ == "__main__":

    main()