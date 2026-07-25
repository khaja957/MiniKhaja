import sys

from PySide6.QtWidgets import QApplication

from window import CompanionWindow

from animation.animation import Animation
from animation.player import AnimationPlayer


app = QApplication(sys.argv)

window = CompanionWindow()

idle = Animation("assets/idle", fps=30)

player = AnimationPlayer(window.pixmap)

player.play(idle)

window.show()

app.exec()