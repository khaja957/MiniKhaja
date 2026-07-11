from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Qt


class PetWidget(QLabel):

    def __init__(self):

        super().__init__()

        self.setAttribute(
            Qt.WA_TranslucentBackground
        )

        self.setScaledContents(True)

        self.resize(180, 180)