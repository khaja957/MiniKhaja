from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QLabel,
    QComboBox,
    QPushButton,
)


class Toolbar(QWidget):

    def __init__(self):
        super().__init__()

        layout = QHBoxLayout(self)

        layout.addWidget(QLabel("Character"))

        self.character = QComboBox()
        self.character.addItem("Mini Khaja")

        layout.addWidget(self.character)

        layout.addStretch()

        self.generate = QPushButton("Generate")

        layout.addWidget(self.generate)