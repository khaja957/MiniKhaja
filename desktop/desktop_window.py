from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QWidget

from pet.sprite_manager import SpriteManager

from core.constants import (
    WINDOW_HEIGHT,
    WINDOW_TITLE,
    WINDOW_WIDTH,
    START_X,
    START_Y,
)


class DesktopPetWindow(QWidget):
    """
    Main transparent window for Mini Khaja.
    """

    def __init__(self):
        super().__init__()

        self.sprite_manager = SpriteManager()

        self.setup_window()
        self.create_pet()

    def create_pet(self):
        """Create the Mini Khaja sprite."""

        self.pet_label = QLabel(self)

        pixmap = self.sprite_manager.get_idle_sprite()

        self.pet_label.setPixmap(pixmap)

        self.pet_label.adjustSize()

        self.pet_label.move(10, 10)

    def setup_window(self):
        """Configure the desktop pet window."""

        self.setWindowTitle(WINDOW_TITLE)

        self.setWindowFlags(
            Qt.FramelessWindowHint
            | Qt.WindowStaysOnTopHint
        )

        self.setAttribute(Qt.WA_TranslucentBackground)

        self.resize(
            WINDOW_WIDTH,
            WINDOW_HEIGHT,
        )

        self.move(
            START_X,
            START_Y,
        )