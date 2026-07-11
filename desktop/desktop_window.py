from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout

from animation.animation_engine import AnimationEngine
from animation.sprite_loader import SpriteLoader
from desktop.pet_widget import PetWidget


class DesktopWindow(QWidget):

    def __init__(self):

        super().__init__()

        self.setWindowFlags(
            Qt.FramelessWindowHint
            | Qt.WindowStaysOnTopHint
        )

        self.setAttribute(Qt.WA_TranslucentBackground)

        self.pet = PetWidget()

        layout = QVBoxLayout()

        layout.setContentsMargins(0, 0, 0, 0)

        layout.addWidget(self.pet)

        self.setLayout(layout)

        self.loader = SpriteLoader()

        self.engine = AnimationEngine()

        self.engine.frame_changed.connect(
            self.pet.show_frame
        )

        idle_frames = self.loader.load("idle")

        self.engine.play(idle_frames)

        self.resize(self.pet.size())