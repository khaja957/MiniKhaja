from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel

from core.config import WINDOW_WIDTH, WINDOW_HEIGHT


class PetWidget(QLabel):

    def __init__(self):

        super().__init__()

        self.setFixedSize(
            WINDOW_WIDTH,
            WINDOW_HEIGHT
        )

        self.setScaledContents(True)

        self.setAlignment(Qt.AlignCenter)

    def show_frame(self, pixmap):

        self.setPixmap(pixmap)